import csv
import json
import os
import requests
import json
from bs4 import BeautifulSoup
from flask import Blueprint, Response, request, jsonify
from urllib.parse import urljoin
from utils.scrape_news import scrape_links
from flask import render_template
from output_thread import output_thread
from utils.spChars import spChars
from utils.related_words import get_related_word
search_bp = Blueprint('search', __name__)

@search_bp.route('/search')
def search():
    tomogatchi = request.args.get('tomogatchi')
    specOrFuncC = request.args.get('specOrFuncC')
    
    queri = request.args.get('q')
    query = queri.replace(' ', '-')
    relWord = get_related_word(queri)
    relWordi = relWord.replace(' ', '-')
    if not relWordi:
        relWordi = "decoy wordi is empty strang ln29 search.py"
    
    if not query:
        return render_template('no_links.html',relWordi=relWordi)        
    
    data = {'json': [], 'links': [], 'text': []}
    retArr = [{'json': []},{'links': []},{'text': []}]

    with open('assets/newssources.csv', 'r') as csvfile:
        urls = [f'https://{row[0]}' for row in csv.reader(csvfile)]

    for url in urls:
        url_data = {'base_url': url, 'json': [], 'links': [], 'text': []}

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        print('[search.py ln53: ] extracting text')
        text = soup.get_text()
        url_data['text'].extend(text)

        print('[search.py ln59]calling scrape_links')
        links = scrape_links(url,query,True)
        url_data['links'].extend(links)
    
        title = soup.title.string if soup.title is not None else ""
        if url_data['json'] or url_data['links'] or url_data['text']:
            print('caching data ...')
            with open(os.path.join('caches', url.replace('/', '_') + '.json'), 'w') as f:
                json.dump(url_data, f)
            print('data cached ...')

            print('reading cache searching for q in cache')
            with open(os.path.join('caches', url.replace('/', '_') + '.json'), 'r') as f:
                data = json.load(f)
                for item in data['links']:
                    if item and len(item) > 0 and query in item and item not in retArr[1]['links']:
                        retArr[1]['links'].append(item)
                    if item and len(item) > 0 and relWordi in item and item not in retArr[1]['links']:
                        print('[search.py ln 94]~~~ITEM: ', item)
                        retArr[1]['links'].append(item)

            print('emptying cache ...')
            try:
                os.remove(os.path.join('caches', url.replace('/', '_') + '.json'))
            except PermissionError:
                print('PermissionError: The file is being used by another process.')
    print('return array[1]:')
    link_html = ""
    for link in retArr[1]['links']:
        if link:
            link_html += f"<h6>{link[12:30]}</h6><ol>"
        else:
            link_html += f"<h6>{url}</h6><ol>"
        link_html += f"<li><a href='{link}'>{link}</a></li>"
        link_html += "</ol>"

    clientresponse = link_html
    output = output_thread(retArr, query, relWordi)
    if not output and not retArr[1]['links']:
        return render_template('no_links.html', relWordi=relWordi)
    
    return render_template('search_results.html', links=retArr[1]['links'], output=output, relWordi=relWordi)


