import re
import requests
import time
from bs4 import BeautifulSoup

wdurl = [
  ("https://idahonews.com/news/local",0),
  ("https://www.kivitv.com/news",1)
  ]

text  = []



def bsoup():
  for t in text:
    soup = BeautifulSoup(t, 'html.parser')
    title = soup.find_all(name='h3', attrs={"class":"ListItem-title"})
    for t in title:
      print(t.string)

def string_split():
  for t in text:
    t = t.split(',')
    for i in t:
      if '"title":"' in i:
        title = i.split(':')
        title = title[1].strip('"')
        print(title)

def req():
  for url, parser in wdurl:
    page = requests.get(url)
    text.append(page.text)
    if parser == 1:
      bsoup()
    else:
      string_split()

req()
