import requests
from bs4 import BeautifulSoup
from time import sleep


def get_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def scrape_tiki(url):

        soup = get_url(url)

        products = soup.find_all('div', {'class':'product-item'})

        data = []

        for div in products:
            try:
              d = {'title':'', 'url':'', 'image_url':'', 'price':''}

              d['url'] = div.a['href']
              d['title'] = div['data-title']
              d['price'] = div['data-price']
              if div.img:
                  d['image_url'] = div.img['src']

              data.append(d)
            except:

              print("We got one error!")

        return data
result = []
for i in range(10):
  sleep(5)
  data= scrape_tiki('https://tiki.vn/dien-thoai-may-tinh-bang/c1789?src=c.1789.hamburger_menu_fly_out_banner&page='+str(i+1))
  print(data)
  result= result+data
print(result)

import pandas as pd
tiki = pd.DataFrame(data = result, columns = result[0].keys())
tiki