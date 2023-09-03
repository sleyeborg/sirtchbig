import json
import requests
from bs4 import BeautifulSoup

def get_related_word(query):
    print('[related_words.py ln6]')
    query = query.replace('-', ' ')  # Replace whitespace with hyphens
    build = 'https://relatedwords.org/relatedto/' + query
    reqs = requests.get(build)
    soup = BeautifulSoup(reqs.content, 'html.parser')
    cont = soup.find_all('script', {'id': 'preloadedDataEl'})
    
    if not cont:
        print('line 60 output_thread no cont empty arr?')
        return []
    
    contstr = cont[0].string
    d = json.loads(contstr)
    
    if d['terms']:
        dd = d['terms'][0]['word']
        print("buildurl; request url; parse url; findin url; stringify url; json url; related word is: ", dd)
        return dd
    else:
        d['terms']='no related words found'
        print("No related words found.")
        return ''
