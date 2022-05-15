import requests
from bs4 import BeautifulSoup

# file1 = open('headers.txt', 'r')
# count = 0

# headers = dict()
  
# while True:
#     count += 1
  
#     # Get next line from file
#     line = file1.readline()
  
#     # if line is empty
#     # end of file is reached
#     if not line:
#         break

#     line = line.strip()
#     line = line.split(": ")
#     headers[line[0]] = line[1]
#     # print(line)
  
# file1.close()
# print(headers)

headers = {'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9', 'cache-control': 'no-cache', 'content-length': '0', 'cookie': 'SFSESSIDGLOMARK=1f66c896708254b645c2cb57be797a9f; _ga=GA1.2.587093900.1652606719; _gid=GA1.2.1742463027.1652606719; _gcl_au=1.1.1186155774.1652606719; _fbp=fb.1.1652606719243.407697338; __zjc7175=5191859997; _gat_gtag_UA_134271598_1=1; _gat_gtag_UA_134125081_1=1; _gat_UA-134271598-1=1; _gat_UA-134125081-1=1', 'dnt': '1', 'origin': 'https://glomark.lk', 'pragma': 'no-cache', 'referer': 'https://glomark.lk/coconut/p/11624', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Linux"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36', 'x-requested-with': 'XMLHttpRequest'}

s = requests.Session()

user_agent = {'User-agent': 'Mozilla/5.0'}

s.headers.update(headers)

url = 'https://glomark.lk/coconut/p/11624'

i = s.get(url)
# print(i)
glomark_soup = BeautifulSoup(i.content, 'html.parser')
product_name_glomark = glomark_soup.find(class_="product-title").findChild().get_text(strip=True)

json_url = 'https://glomark.lk/product-page/variation-detail/' + url.rsplit('/', 1)[-1]
r = s.post(json_url)
price_glomark = float(r.json()['price'])

print(product_name_glomark)
print(price_glomark)