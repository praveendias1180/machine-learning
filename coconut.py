import requests
import json
import re

import sys
from bs4 import BeautifulSoup

#Imitate the Mozilla browser.
user_agent = {'User-agent': 'Mozilla/5.0'}


def compare_prices(product_laughs,product_glomark):
    #TODO: Aquire the web pages which contain product Price

    laughs_res = requests.get(product_laughs)
    
    #TODO: LaughsSuper supermarket website provides the price in a span text.

    laughs_soup = BeautifulSoup(laughs_res.content, 'html.parser')
    laughs_tag = laughs_soup.findAll(class_="price")[1].get_text()

    price_laughs = float(laughs_tag[3:])

    product_name_laughs = laughs_soup.find(class_="product-name").findChild().get_text(strip=True)

    #TODO: Glomark supermarket website provides the data in jason format in an inline script.
    #You can use the json module to extract only the price
    
    headers = {'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9', 'cache-control': 'no-cache', 'content-length': '0', 'cookie': 'SFSESSIDGLOMARK=1f66c896708254b645c2cb57be797a9f; _ga=GA1.2.587093900.1652606719; _gid=GA1.2.1742463027.1652606719; _gcl_au=1.1.1186155774.1652606719; _fbp=fb.1.1652606719243.407697338; __zjc7175=5191859997; _gat_gtag_UA_134271598_1=1; _gat_gtag_UA_134125081_1=1; _gat_UA-134271598-1=1; _gat_UA-134125081-1=1', 'dnt': '1', 'origin': 'https://glomark.lk', 'pragma': 'no-cache', 'referer': 'https://glomark.lk/coconut/p/11624', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Linux"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36', 'x-requested-with': 'XMLHttpRequest'}

    s = requests.Session()

    user_agent = {'User-agent': 'Mozilla/5.0'}

    s.headers.update(headers)

    url = product_glomark

    i = s.get(url)

    glomark_soup = BeautifulSoup(i.content, 'html.parser')
    product_name_glomark = glomark_soup.find(class_="product-title").findChild().get_text(strip=True)

    json_url = 'https://glomark.lk/product-page/variation-detail/' + url.rsplit('/', 1)[-1]
    r = s.post(json_url)
    price_glomark = float(r.json()['price'])
    
    #TODO: Parse the values as floats, and print them.
    
    print('Laughs  ',product_name_laughs,'Rs.: ' , price_laughs)
    print('Glomark ',product_name_glomark,'Rs.: ' , price_glomark)
    
    if(price_laughs>price_glomark):
        print('Glomark is cheaper Rs.:',price_laughs - price_glomark)
    elif(price_laughs<price_glomark):
        print('Laughs is cheaper Rs.:',price_glomark - price_laughs)    
    else:
        print('Price is the same')

laughs_coconut = 'https://scrape-sm1.github.io/site1/COCONUT%20market1super.html'
glomark_coconut = 'https://glomark.lk/coconut/p/11624'
compare_prices(laughs_coconut, glomark_coconut)