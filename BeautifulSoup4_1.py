import requests
from bs4 import BeautifulSoup

url='https://www.google.com/search? q=Python'
html= requests.get(url).content
soup= BeautifulSoup(html,'html.parser')

#Retrieve all of the anchor tags
tags= soup('a')
for tag in tags:
    print(tag.get('href'))