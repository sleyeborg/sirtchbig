from bs4 import BeautifulSoup, Tag, Script
import requests
import csv
import re
from urllib.parse import urlparse
from urllib.parse import unquote
#use urllib to parse urls

def scrape_products(q):
    url_pattern = r"https://[^;]+"
    #this is supposed to do everything search.py does so that we can split off and abstract search.py. 
    print('begin scrape_products')
    #takes a q input. 
    chozer = []
    #gets a list of links from a csv file. 
    with open('assets/specify.csv', 'r') as csvfile:
        urls = [f'https://{row[0]}' + q for row in csv.reader(csvfile)]
    
    #in each link inside of links from csv, looks for all ahref tags.
    linkArr0 = []
    datuminArr = []
    #print('urls',urls)
    for url in urls:
        #print('url',url)
        response = requests.get(url)
        #print('response',response)
        soup = BeautifulSoup(response.content, 'html.parser')
        body = soup.find('body')
        #print(body)
        if body is not None:
            i = 0
            j = 0
            base_url = url[39:45]
            #print("1234554321",base_url)
            for tag in body:
                #print('tag: ',i, tag )
                i+=1
                for tagger in tag:
                    
                    #print('tagger',j,' in tag',i, tagger)
                    j+=1
                    if isinstance(tagger, Tag):
                        if not str(tagger).startswith("<script"):
                            print("type: ",type(tagger))
                            print("")
                            innerlinks = str(tagger)
                            urls = re.findall(url_pattern, innerlinks)                            
                            linkArr0.append(urls)
                    
            
        else:
            print('No <body> tag found in the HTML')
        #all_text = soup.get_text()
        #all_links = soup.find_all('a')
    linkArr1 = []
    imgarr = []
    roots = []
    for array in linkArr0:
        for item in array:
                decoded_link = unquote(item)
                modified_link = decoded_link[:-4]
                if "policies.google" in item:
                    print('removed a policies.google url')
                elif "support.google" in item:
                    print('removed a support.google uurl')
                elif "google.com/preferences" in item:
                    print('removed googlepreferences url')
                elif "google.com/search?ie=UTF-8" in item:
                    print('removed a google.com homepage url')
                elif "accounts.google.com/ServiceLogin" in item:
                    print('removed a googleaccounts login')
                elif "maps.google.com/maps?q" in item:
                    print('removed a googlemaps url')
                elif "google.com/imgres?imgurl" in item:
                    imgarr.append(modified_link)
                    print("ln 73 scrape_product.py appended modified_link to imgarr" )
                elif "google.com/search?" in item:
                    roots.append(modified_link)
                    print("roots array is an array of root google dorks")
                else:
                    linkArr1.append(modified_link)
    print('linkArr1: ', linkArr1)
       
    print("00000000000\n11111111111\n10000000000\n01000000000\n00100000000\n00010000000\n00001000000\n00000100000\n00000010000\n00000001000\n00000000100\n00000000010\n00000000001\n11111111111\n00000000000")
    return linkArr1




