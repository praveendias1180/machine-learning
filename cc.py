import requests
import json

from bs4 import BeautifulSoup

#Imitate the Mozilla browser.
user_agent = {'User-agent': 'Mozilla/5.0'}


def compare_prices(product_laughs,product_glomark):

    html = requests.get(product_laughs).content
    soup = BeautifulSoup(html, 'html.parser')
    price_laughs = soup.find("span", {"class": "regular-price"}).get_text()
    product_name_laughs = soup.find("div", {"class": "product-name"}).get_text()
    price_laughs = float(price_laughs.replace('Rs.', ''))
    
    html = requests.post(product_glomark).content
    soup = BeautifulSoup(html, 'html.parser')
    sc = soup.find('script', type='application/ld+json').get_text()
    sc = json.loads(sc)
    product_name_glomark = sc['name']
    price_glomark = float(sc['offers'][0]['price'])
    
    print('Laughs  ',product_name_laughs,'Rs.: ' , price_laughs)
    print('Glomark ',product_name_glomark,'Rs.: ' , price_glomark)
    
    if(price_laughs>price_glomark):
        print('Glomark is cheaper Rs.:',price_laughs - price_glomark)
    elif(price_laughs<price_glomark):
        print('Laughs is cheaper Rs.:',price_glomark - price_laughs)    
    else:
        print('Price is the same')

# laughs_coconut = 'https://scrape-sm1.github.io/site1/COCONUT%20market1super.html'
# glomark_coconut = 'https://glomark.lk/coconut/p/11624'

# laughs_coconut = 'https://scrape-sm1.github.io/site1/FLORA%20FACIAL%20TISSUES%202%20X%20160%20BOX%20-%20HOUSEHOLD%20-%20Categories%20market1super.com.html'
# glomark_coconut = 'https://glomark.lk/flora-facial-tissues-160s/p/10470'

# laughs_coconut = 'https://scrape-sm1.github.io/site1/Crimson%20Bread%20Sliced%20market1super.com.html'
# glomark_coconut = 'https://glomark.lk/top-crust-bread/p/13676'

laughs_coconut = 'https://scrape-sm1.github.io/site1/COCA%20COLA%202L%20(PET)%20-%20BEVERAGES%20-%20Categories%20market1ssuper.com.html'
glomark_coconut = 'https://glomark.lk/coca-cola-pet-2l/p/9613'


compare_prices(laughs_coconut, glomark_coconut)