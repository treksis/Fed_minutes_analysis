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

    for element in header_list[1:10]:
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
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20210616.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20210428.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20210317.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20210127.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20201216.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20201105.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20200916.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20200729.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20200610.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20200429.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20200315.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20200129.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20191211.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20191030.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20190918.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20190731.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20190619.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20190501.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20190320.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20190130.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20181219.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20181108.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20180926.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20180801.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20180613.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20180502.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20180321.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20180131.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20171213.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20171101.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20170920.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20170726.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20170614.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20170503.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20170315.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20170201.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20161214.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20161102.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20160921.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20160727.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20160615.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20160427.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20160316.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20160127.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20151216.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20151028.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20150917.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20150729.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20150617.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20150429.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20150318.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20150128.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20141217.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20141029.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20140917.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20140730.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20140618.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20140430.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20140319.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20140129.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20131218.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20131030.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20130918.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20130731.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20130619.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20130501.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20130320.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20130130.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20121212.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20121024.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20120913.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20120801.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20120620.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20120425.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20120313.htm',
 'https://www.federalreserve.gov/monetarypolicy/fomcminutes20120125.htm']


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