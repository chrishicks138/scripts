import time
import re
import urllib.error as error
import requests
import random
import threading
import time
import searchterm
import threading
from collections import deque
from concurrent.futures import ThreadPoolExecutor
import sql
import text.textSQL as textSQL
import text.textConfig as textConfig
import proxy_check.sql as proxySQL
import config
import proxy_check.proxy_config as proxyConfig
import proxy_check.ip_get as proxyGet
from bs4 import BeautifulSoup


checked_urls = []
pending      = []
unique       = []
result_list  = []
proxy_list   = []
queue = []

sql.main()
proxySQL.main()
textSQL.main()
proxySQL.get_all(proxyConfig.DATABASE)
for ip, port in proxySQL.db_results:
    proxy_list.append(ip+":"+port)

'''
try:
  searches = set(searchterm.search())
except error:
  pass
'''

_lock = threading.Lock()

# for url in list(searches):
url = "https://www.tabletmag.com/sections/news/articles/china-covid-lockdown-propaganda"
result_list.append(url)

def clearQueue():
    if len(queue) > 100:
        for idx, q in enumerate(queue):
            downloaded = False
            url_submit(url, downloaded)
            queue.pop(idx)
        return

def queueSort(result):
    unique = []
    for i, url in enumerate(result):
        if len(result) > 1:
            if len(result) > 2:
                queue.append(url)
                result.pop(i)
            elif len(unique) < 2:
                if len(queue) > 0:
                    unique.append(queue[:1])
                    queue.pop(i)
        unique.append(url)
        result.pop(i)
    return unique

def unique_urls(result):
    clearQueue()
    with ThreadPoolExecutor(max_workers=2) as executor:
        for index, item in enumerate(queueSort(result)):
            executor.submit(download, (item))
        print("PROXIES", len(proxy_list), "QUEUED", len(queue), "DOWNLOADING", len(queueSort(result)))

def url_submit(url, downloaded):
    item = (url,downloaded)
    sql.add_AP(config.DATABASE, item)

def submit(unique, ptag, url):
    if len(ptag) != 0:
        for p in ptag:
            text = p.get_text()
            item = (url, text)
            textSQL.add_AP(textConfig.DATABASE, item)
    else:
        pass
    downloaded = True
    for index, link in enumerate(unique):
        url_submit(url, downloaded)
        pending.append(link)
        unique.pop(index)
    unique_urls(pending)

def parse(html):
    regex = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    unique = re.findall(regex,html)
    unique = set(unique)
    unique = list(unique)
    return unique

def download(url):
    try:
        idx = random.randint(0, len(proxy_list) - 1)
        proxy = { "http" : 'http://'+proxy_list[idx] }
        page = requests.get(url, proxies=proxy, timeout=60)
        soup = BeautifulSoup(page.content, 'html.parser')
        ptag = soup.find_all('p')
        html = page.text
        if page.status_code != 200:
            proxy_list.pop(idx)
            return
        else:
            unique = parse(html)
            if len(unique) < 1:
                print("No links found!")
                proxy_list.pop(idx)
                return
            else:
                submit(unique, ptag, url)
                checked_urls.append(url)
            return
    except requests.exceptions.RequestException as e:
        # print(e)
        proxy_list.pop(idx)
        download(url)
    except UnicodeError as e:
        print(e)
        return



unique_urls(result_list)

