import requests
from bs4 import BeautifulSoup

URL = 'http://www.aphorisme.ru/random/?q=2329'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'accept': '*/*'}
HOST = 'https://auto.ria.com'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content_phrase(html):
    res = ''
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='rendom_aph')
    for quote in items:
        res += quote.text
    return res

def get_content_author(html, quoteEror=None):
    res = ''
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('div', class_='rendom_aph_v')
    if items is None:
        return res
    else:
        return items.text

def parse():
    global res
    html = get_html(URL)
    if html.status_code == 200:
        phrase = get_content_phrase(html.text)
        author = get_content_author(html.text)
        res = phrase + '\n' + author
    else:
        print('Error')
    return res
