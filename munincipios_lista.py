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
                arquivo.write(link['href'] + '\n')

        driver.quit()
    except:
        pass

url = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# Acre 1
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/ac/" + str(i)
    collect_urls(link)

# Amazonas 2
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/am/" + str(i)
    collect_urls(link)

# Bahia 3
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/ba/" + str(i)
    collect_urls(link)

# Distrito Federal 4
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/df/" + str(i)
    collect_urls(link)

# Goias 5
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/go/" + str(i)
    collect_urls(link)

# Minas Gerais 6
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/mg/" + str(i)
    collect_urls(link)

# Mato Grosso 7
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/mt/" + str(i)
    collect_urls(link)

# Paraiba 8
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/pb/" + str(i)
    collect_urls(link)

# Piaui 9
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/pi/" + str(i)
    collect_urls(link)

# Rio de Janeiro 10
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/rj/" + str(i)
    collect_urls(link)

# Rondônia 11
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/ro/" + str(i)
    collect_urls(link)

# Rio Grande so Sul 12
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/rs/" + str(i)
    collect_urls(link)

# Sergipe 13
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/se/" + str(i)
    collect_urls(link)

# Tocantins 14
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/to/" + str(i)
    collect_urls(link)

# Alagoas 15
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/al/" + str(i)
    collect_urls(link)

# Amapá 16
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/ap/" + str(i)
    collect_urls(link)

# Ceará 17
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/ce/" + str(i)
    collect_urls(link)

# Espirito Santo 18
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/es/" + str(i)
    collect_urls(link)

# Maranhão 19
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/ma/" + str(i)
    collect_urls(link)

# Mato Grosso do Sul 20
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/ms/" + str(i)
    collect_urls(link)

# Pará
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/pa/" + str(i)
    collect_urls(link)

# Pernanbuco 
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/pe/" + str(i)
    collect_urls(link)

# Paraná 21
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/pr/" + str(i)
    collect_urls(link)

# Rio Grande do Norte 22
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/rn/" + str(i)
    collect_urls(link)

# Roraima 23
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/rr/" + str(i)
    collect_urls(link)

# Santa Catarina 24
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/sc/" + str(i)
    collect_urls(link)

# São Paulo 25
for i in url:
    link = "https://leismunicipais.com.br/cidades-por-estado/sp/" + str(i)
    collect_urls(link)