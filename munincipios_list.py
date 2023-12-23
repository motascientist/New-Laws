from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup

def collect_urls(site):

    try:
        url = site
        chrome_driver_path = "/usr/bin/chromedriver"
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = "/usr/bin/google-chrome"
        chrome_options.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        sleep(2)
        
        page_html = driver.page_source
        soup = BeautifulSoup(page_html, 'html.parser')
        
        block = soup.find('ul', class_='founds')
        links = block.find_all("a")
        
        with open("munincipios.txt", "a") as arquivo:
            for link in links:
                print(link['href'])
                arquivo.write(link['href'][1:] + '/' + '\n')

        driver.quit()
    except:
        pass

urls = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
links = ['ac','am','ba','df','go','mg','mt','pb','pi','rj','ro','rs','se','to','al','ap','ce','es','ma','ms','pa','pe','pr','rn','rr','sc','sp']

for link in links:
    for url in urls:
        print(url)
        site = f"https://leismunicipais.com.br/cidades-por-estado/{link}/" + str(url)
        collect_urls(site)

