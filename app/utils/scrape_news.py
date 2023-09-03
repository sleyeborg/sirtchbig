import csv
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

def isPartOfWord(queri, item):
    pattern = r'\b{}\b'.format(re.escape(queri))
    return re.search(pattern, item, flags=re.IGNORECASE) is not None

def scrape_links(url, queri, specify):
#    print(specify)
    links = []

    if url.startswith('mailto:'):
#        print("Found mailto URL:", url)
        return links
    if url.startswith('javascript:void(0)'):
#        print('found javascript:void(0)')
        return links

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    base_url = response.url

    counter = 0
    for link in soup.find_all('a'):
        href = link.get('href')
        if href is not None and len(href) > 0:
            if 'http' not in href:
                href = urljoin(base_url, href)
            links.append(href)
#            print('69696[SCRAPE.PY LM 35] LINKS[] number: ')
#            print('base_url:  ', base_url, "        ")
#            print('<<<<<<<<<<< href:  ', href, '<<<<<<<<<')
#            print(counter, "~~~~~~~~")

            counter += 1

    links_copy = links.copy()
#    print('[scrap.py ln44] links[:40]:  ^8080808080808^', links)
    for item in links_copy:
        if not isPartOfWord(queri, item):
            links.remove(item)
#    print('[scrap.py ln44] links[:40]:  ^^', links)
    return links

def read_urls_from_csv(csv_path):
    with open(csv_path, 'r') as csvfile:
        urls = [f'https://{row[0]}' for row in csv.reader(csvfile)]
    return urls
