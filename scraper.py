# Importing libraries
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import pandas as pd
import re
import time
import os
import boto3

# AWS

if os.environ.get('AWS_ENV') == 'dev':
            client = boto3.client('s3',
                region_name=os.environ.get('AWS_DEFAULT_REGION'),
                aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
            )        
else:
    session = boto3.Session()
    client = session.client('s3')

# Defining the site URL
site = 'https://leismunicipais.com.br/legislacao-municipal/'

# Define a function to scrape data
def leis(site):
    # Get the current date
    today = datetime.today().strftime('%Y-%m-%d')

    # Initialize lists to store data
    county_lst = []
    date_lst = []
    decree_lst = []
    text_lst = []
    link_lst = []

    # Read the list of municipalities from the file
    with open("munincipios.txt", 'r') as file:
        municipalities = file.read().splitlines()

    # Loop through each municipality
    for municipality in municipalities:
        url = f"{site}{municipality[21:]}"
        print(f"Scraping data for: {url}")

        # Retry logic
        max_retries = 3
        retries = 0
        while retries < max_retries:
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                box = soup.find(class_="container main")
                contents = box.find_all(class_="content")

                # Check if contents exist
                if len(contents) > 2:
                    decretos = contents[2].find_all(class_='title')
                    texts = contents[2].find_all(class_='description')
                    links = contents[2].find_all(class_='law')  # The second box has the recent laws approved

                    # Extract date and decree number
                    for decreto in decretos:
                        match = re.search(r'leis-de-(.+?)/', municipality)
                        match = match.group(1)
                        county_lst.append(match)

                        standard = r"\d{2}/\d{2}/\d{4}"
                        data = re.findall(standard, decreto.text)
                        date_lst.append(data[0])
                        decree_lst.append(decreto.text)

                    # Extract text and links
                    for text in texts:
                        text_lst.append(text.text)

                    for link in links:
                        link_lst.append('https://leismunicipais.com.br' + link['href'])

                break  # Successful scrape, exit the retry loop
            except requests.exceptions.RequestException as e:
                if isinstance(e, requests.exceptions.ConnectTimeout):
                    print(f"Request failed with ConnectTimeout: {e}")
                    retries += 1
                    if retries < max_retries:
                        print(f"Retrying in 5 seconds...")
                        time.sleep(5)
                    else:
                        print("Max retries reached. Skipping this URL.")
                        break
                else:
                    print(f"Request failed with error: {e}")
                    break  # Continue to the next URL for non-timeout errors

    # Create a DataFrame with the scraped data
    df = pd.DataFrame({
        "Date": date_lst,
        'County': county_lst,
        'Decree': decree_lst,
        "Text": text_lst,
        "Link": link_lst
    })

    # Convert the 'Date' column to date format
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y').dt.date

    json_data = df.to_json(orient='records', indent=4)

    with open(f"{today}.json", 'w') as json_file:
        json_file.write(json_data)

    out_file_path = f'{today}.json'
    client.put_object(Body=open(out_file_path, 'rb'), Bucket='ai-colected-data', Key=f"leis-munincipais/{today}.json")

    os.remove(out_file_path)
    print('>>> Uploaded to S3!')

    # Create an EC2 client
    ec2_client = boto3.client('ec2',
        region_name="sa-east-1",
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'))

    # Replace "client" with "ec2_client" in your code
    ec2_client.stop_instances(InstanceIds=["Your-Instance-id"])

# Call the function to scrape data
leis(site)
