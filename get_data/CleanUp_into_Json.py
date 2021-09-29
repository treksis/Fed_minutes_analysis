from collections import defaultdict
from bs4 import BeautifulSoup
import requests
import re
import time
import os
import json
from Selenium_scrap import scrap_links

def get_article(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    article = soup.find("div", {"id": "article"})
    return article    

def get_paragraphs(first_paragraph):
    current_paragraph = first_paragraph
    while True:
        yield current_paragraph

        current_paragraph = current_paragraph.find_next('p')
        if not current_paragraph or (current_paragraph.strong and current_paragraph.strong.text.strip() != ''):
            break

def data_clean(article):
    header_list = []
    
    article.findAll("strong")
    
    for header in article.findAll("strong"):
        header_list.append(header.text)
        
    d = defaultdict()

    for element in header_list:
        if element not in d:
            d[element] = []

        for p in get_paragraphs(article.select_one(f'p:-soup-contains("{element}")')):
            paragraph = p.text
            paragraph = re.sub("\n", " ", paragraph)

            d[element].append(paragraph)
    
    for k,v in d.items():
        d[k] = ''.join(v)

    return d

# k will be replaced by file from selenium
# k = scrap_links()

k = ['https://www.federalreserve.gov/monetarypolicy/fomcminutes20210728.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20210428.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20210317.htm']


for i in k:
    time.sleep(2)
    h = get_article(i)
    parsed = data_clean(get_article(i))
    
    if os.path.isfile(str(i[-12:])+".json"):
        print("File has been added")
        parsed = data_clean(h)
        #print(parsed.keys())
        json_string = json.dumps(parsed)
        f = open(str(i[-12:])+".json","w")
        f.write(json_string)
        f.close()
    
    else:
        print("database doesn't exist so it was created!")
        json_string = json.dumps(parsed)
        f = open(str(i[-12:])+".json","w")
        f.write(json_string)
        f.close()