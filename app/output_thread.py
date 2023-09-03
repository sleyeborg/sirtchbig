import csv
import json
import os
import requests
import json
from bs4 import BeautifulSoup
from flask import Blueprint, Response, request, jsonify
from urllib.parse import urljoin
from utils.scrape_news import scrape_links
from utils.related_words import get_related_word
from flask import render_template
import time

def output_thread(retArr,query,relWordi):
    print("begin output_thread...")
    print("retArr:  ", retArr)
    print("query:  ", query)
    print("relWordi:  ", relWordi)
    response_data = {'json': [], 'links': [], 'text': []}
    start_time = time.perf_counter()
    for item in retArr[1]['links']:
        links = scrape_links(item,relWordi,True)
        #print('[output_thread.py ln 20] links[:40]:', links[:40])
        if not links:
            continue
        response_data['links'].extend(links)
        for link in links:
            if query in link:
                response_data['links'].append(link)
    
    elapsed_time = (time.perf_counter() - start_time) * 1000
    print(f"[o_tln29] formatting Elapsed time: {elapsed_time:.2f} ms")

    print("[o_t ln31] opening     caches/output_cache.json', 'w ")
    # Cache the data in a file
    with open('caches/output_cache.json', 'w') as f:
        f.truncate(0)
        json.dump(response_data, f)
    print('[o_t ln36] READING FROM OUTPUT CACHEDOT JSON!!!!!!!!!')
    # Read the cached data
    with open('caches/output_cache.json', 'r') as f:
        cached_data = f.read()
    json_object = json.loads(cached_data)
    oIO=[]
    for link in json_object['links']:
        if link not in oIO:
            oIO.append(link)
        
    innerArr = []
    if relWordi is not '':
        for line in oIO:
            if relWordi in line and line not in innerArr and line not in retArr[1]['links']:
                innerArr.append(line)
    #remove duplicates by converting to a set then back to a list.     
    innerArr = list(set(innerArr))           
    
    os.remove(os.path.join('caches', 'output_cache.json'))
    return innerArr
