import requests
from lxml import html
import pandas as pd
items = []
url = 'https://scrapeme.live/shop/page/{}/'
for i in range(1, 11):
    response = requests.get(url=url.format(i))
    html_text = response.text
    html_response = html.fromstring(html_text)
    rows = html_response.xpath('//ul[@class="products columns-4"]//a[@class="woocommerce-LoopProduct-link woocommerce-loop-product__link"]')
    for row in rows:
        product_url = "".join(row.xpath('@href'))
        product_name = "".join(row.xpath('h2[@class="woocommerce-loop-product__title"]/text()'))
        product_price=",".join(row.xpath('span[@class="price"]/span[@class="woocommerce-Price-amount amount"]/text()'))
        item = {
            'name':product_name,
            'price':product_price,
            'url':product_url
        }
        items.append(item)
#to convert to csv
df=pd.DataFrame(items)
df.to_csv("scrapme_live.csv",index=False)
