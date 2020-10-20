import time
import re
import urllib.error as error
import requests
import time
import searchterm
import threading
from collections import deque
import concurrent.futures as future
import sql
import config


try:
  searches = set(searchterm.search())
except error:
  pass

sql.get_all(config.DATABASE)
url_list = sql.db_results
_lock = threading.Lock()

def unique_urls(unique):
    with future.ThreadPoolExecutor(max_workers=10) as executor:
        for index, item in enumerate(unique):
            print("URL: "+item, "URL LIST INDEX: "+str(index)+'/'+str(len(unique)))
            executor.submit(download, item, unique)
            downloaded = True
            item = (item,
                    downloaded,
                    )
            sql.add_AP(config.DATABASE, item)
            time.sleep(.5)

def download(url):
    try:
        page = requests.get(url, timeout=5)
        html = page.text
        regex = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
        url = re.findall(regex,html)
        urls = set(url)
        unique = list(urls)
        unique_urls(unique)
        return
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
        return
    except UnicodeError as e:
        print(e)
        return


sql.main()
for url in list(searches):
    url_list.append(url)
for u in url_list:
    if u[1] is True:
      print("URL: "+u[0])
      download(u[0])
    time.sleep(1)
