import requests
from bs4 import BeautifulSoup

params = {
    'wpcategory': 'Информатика',
}

response = requests.get(
    'https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:RandomInCategory',
    params=params)


bs = BeautifulSoup(response.text, 'lxml')
print(response.url)
print(bs.find('title'))
