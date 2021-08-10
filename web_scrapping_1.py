import requests
from lxml import html
import pandas as pd
items = []
url = 'https://quotes.toscrape.com/page/{}/'
for i in range(1, 3):
    response = requests.get(url=url.format(i))
    html_text = response.text
    html_response = html.fromstring(html_text)

    rows = html_response.xpath('//div[@class="quote"]')
    for row in rows:
        quote = row.xpath('span[@class="text"]/text()')
        author = row.xpath('span/small[@class="author"]/text()')
        tags=",".join(row.xpath('div[@class="tags"]/a[@class="tag"]/text()'))
        item = {
            'quote': quote,
            'author': author,
			'tags':tags
        }
        items.append(item)
df=pd.DataFrame(items)
df.to_csv("scrapping_quote.csv",index=False)
