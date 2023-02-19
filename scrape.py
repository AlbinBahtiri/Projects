
import requests

from bs4 import BeautifulSoup

import pandas as pd

books = []

for i in range(1,5):
  url = f"https://books.toscrape.com/catalogue/page-{i}.html"
  response = requests.get(url)
  response = response.content
  soup = BeautifulSoup(response, 'html.parser')
  ol = soup.find('ol')
  articles = ol.find_all('article', class_='product_pod')
  for article in articles:
    image = article.find('img')
    title = image.attrs['alt']
    starTag = article.find('p')
    star = starTag['class'][1]
    price = article.find('p', class_='price_color').text
    price = float(price[1:])
    books.append([title, star, price])
    

df = pd.DataFrame(books, columns=['Title', 'Star Rating', 'Price'])
df.to_csv('books.csv')

#https://www.youtube.com/watch?v=MH3641s3Roc