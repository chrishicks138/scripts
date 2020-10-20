import re
import requests
import time

count = 0
wdurl = "https://idahonews.com/news/local"

page = requests.get(wdurl) # request page.
html = page.text # convert data to text.
print(str(page.status_code)+'\r\n')
textall = re.findall('(["Local","News"],.*)',str(html)) # find first match of word "value", which is next to the data we need.
if textall:
  for text in textall:
    mugshotr = text.rsplit("")[1] # split text right of searched text, which is the data we need.
    namer = text.rsplit("class='myNameTitle'><strong>")[1] # split text right of searched text, which is the data we need.

    mugshot = mugshotr.rsplit(" class")[0] # split string so we get river flow value and date
    name = namer.rsplit("</strong>")[0] # split string so we get river flow value and date
    print(name)

'''
    river_flow_rate_file_name = str(river_flow_rate_file_name).replace(" ","_") # replace spaces with underscores


    url1 = 'http://127.0.0.1:3333/api/river_flow_rates/'+line
    data = {"site": line, "flowrate": river_flow_rate_file_name}
    r = requests.post(url1, verify=False, json=data)
    print(count)
    print(str(r.status_code)+'\r\n')
  time.sleep(3)
'''
