import os
import json
#from scrape import scrapeURL

def spChars(query):
    try:
        data = {'json': [], 'links': [], 'text': []}
        retArr = [{'json': []}, {'links': []}, {'text': []}]
        qEnc = query.replace(' ', '')
        #urls = searchUrls(qEnc)
        print('DEBUG: Query:', query)
        print('DEBUG: Encoded Query:', qEnc)
        print('DEBUG: Current working directory:', os.getcwd())
        print('DEBUG: Contents of utilUtil directory:', os.listdir('./utilUtil'))
        print('DEBUG: Contents of caches directory:', os.listdir('./caches'))
        print('IM A GOOFY GRUBER urls:', qEnc)
        
        return retArr
    except Exception as e:
        print('ERROR:', e)


'''
def spChars(query):
    data = {'json': [], 'links': [], 'text': []}
    retArr = [{'json': []}, {'links': []}, {'text': []}]
    print('HWY 2 DA THANGERROZNE')
    return retArr
'''


'''

def spChars(query):
    """Encode special characters in the search query."""
    encoded_query = query.replace(' ', '%20')
    return encoded_query
'''
