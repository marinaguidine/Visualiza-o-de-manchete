import requests
from bs4 import BeautifulSoup

url= 'https://tribunademinas.com.br/noticias/cultura'

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')

    noticias = soup.find_all('div', class_='col-sm-12')

    for noticia in noticias:
        manchete = noticia.find('h2')
        if manchete:
            print(manchete.text)
else:
    print("Falha na requisição: Status Code", response.status_code)
