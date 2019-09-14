#Program to Download images from a https::{} web_page

import requests #obtener datos: URL de la imagen
from bs4 import BeautifulSoup #permite Parsear el documento querido
from urllib.request import urlretrieve


def run():
    
    for i in range(5,11):
        response = requests.get(f'https://xkcd.com/{i}')
        soup = BeautifulSoup(response.content, 'html.parser')
        image_container = soup.find(id="comic")

        image_url = image_container.find('img')['src']
        image_name = image_url.split('/')[-1]
        print(f'Downloading image {image_name}')

        urlretrieve(f'https:{image_url}', image_name)


if __name__ == '__main__':
    run()
