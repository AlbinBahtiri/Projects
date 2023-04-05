import requests
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from selenium import webdriver

r=requests.get('https://gjirafa50.com/kompjuter-laptop-server-1/kompjuter-1/?rel=1')

print(r)
#print(r.content)


url=('https://gjirafa50.com/kompjuter-laptop-server-1/kompjuter-1/?rel=1')

r=requests.get(url)
print(r.status_code)

soup=BeautifulSoup(r.text,'html.parser')

produktet=soup.find_all('div', class_="ty-grid-list__item-name")

prodi=[]
for produkti in produktet:
    prodi.append(produkti.find('a',{'class':'product-title'}).text)
print(prodi)

cmimet=soup.find_all('span',{'class':'ty-price-num'})

l=[span.get_text()for span in cmimet]
print(l)


cmimet_ok=[x for x in l if "€" not in x]

data=pd.DataFrame()



data['Produkti'] = prodi
data['Cmimi']= cmimet_ok
print(data)