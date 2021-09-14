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
import NLP

checked_urls = []
result_list  = []
proxy_list   = []
queue = []
good_proxies = []

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
url = "https://news.ycombinator.com"
result_list.append(url)


class crawler():
    def __init__(self):
        self.queue = []

    def clearChecked(self):
        if len(checked_urls) >= 5 * 1000:
            for idx, url in enumerate(checked_urls):
                downloaded = True
                self.url_submit(url, downloaded)
                checked_urls.pop(idx)
            return

    def clearQueue(self):
        if len(queue) >= 100:
            for idx, q in enumerate(queue):
                downloaded = False
                self.url_submit(url, downloaded)
                self.queue.pop(idx)

    def queueSort(self, result):
        self.pending = []
        for i, url in enumerate(result):
            if len(result) > 1:
                if len(result) > 20:
                    print("APPENDING")
                    queue.append(url)
                    result.pop(i)
                elif len(result) < 20:
                    if len(queue) > 0:
                        print("PENDING")
                        self.pending.append(queue[:1][0])
                        queue.pop(0)
            if not any(checked for checked in checked_urls):
                print(url)
                self.pending.append(url)
            elif len(queue) > 1:
                self.pending.append(queue[:1][0])
                queue.pop(0)
            result.pop(i)
        self.clearQueue()
        del result
        return self.pending

    def unique_urls(self, result):
        self.clearChecked()
        with ThreadPoolExecutor(max_workers=1) as executor:
            for index, item in enumerate(self.queueSort(result)):
                executor.submit(crawlDownload().download, (item))
            print("PROXIES",
                  len(proxy_list),
                  "QUEUE",
                  len(queue),
                  "DOWNLOADING",
                  len(self.pending),
                  "CHECKED",
                  len(checked_urls),
                  "DB",
                  len(sql.get_all(config.DATABASE))
                  )
            del self.pending
            return


class crawlDownload():
    def __init__(self):
        pass

    def url_submit(self, url, downloaded):
        if not any(result for result in sql.get_all(config.DATABASE)):
            item = (url,downloaded)
            sql.add_AP(config.DATABASE, item)

    def parse(self, html):
        regex = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
        unique = re.findall(regex,html)
        unique = set(unique)
        unique = list(unique)
        return unique

    def download(self, url):
        try:
            idx = random.randint(0, len(proxy_list) - 1)
            proxy = { "http" : 'http://'+proxy_list[idx] }
            page = requests.get(url, proxies=proxy, timeout=10)
            html = page.text
            if page.status_code != 200:
                proxy_list.pop(idx)
            else:
                
                NLP.Process(html)
                
                unique = self.parse(html)
                if len(unique) < 1:
                    proxy_list.pop(idx)
                    return
                else:
                    #print(proxy_list[idx], "good!")
                    checked_urls.append(url)
                    print(unique)
                    crawler().unique_urls(unique)
                    good_proxies.append(proxy_list[idx])
                    print(len(good_proxies))
                    return
                    
            del unique
            del html
            del page
        except requests.exceptions.ProxyError as e:
            # print(e)
            #print(proxy_list[idx], "bad!")
            proxy_list.pop(idx)
            self.download(url)
        except requests.exceptions.RequestException as e:
            #print(e)
            return
        except UnicodeError as e:
            print(e)
        return


crawler().unique_urls(result_list)

