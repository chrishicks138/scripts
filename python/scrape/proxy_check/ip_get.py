import requests
import proxy_check.proxy_config as config
import proxy_check.sql as db
from geoip import geolite2

checked_ip_list = []
print("Initializing Proxy Database")
db.main()
socksList = [
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt",
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
        "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
]

for index, proxies in enumerate(socksList):
    print("Downloading list", index, "...")
    ips = requests.get(proxies)
    ip_list = ips.text.splitlines()
    ip = [ip.split(':') for ip in ip_list]
    ip_list = [(i[0], i[1]) for i in ip[3:]]
    print(len(ip_list), "Proxies found...")
    for ip, port in ip_list:
        try:
            match = geolite2.lookup(ip)
            if match is not None:
                if match.country == 'US':
                    checked_ip_list.append((ip, port))
        except:
            pass

print(len(checked_ip_list), "US proxies about to be inserted to database")
db.get_all(config.DATABASE)
for ip, port in checked_ip_list:
    if not any(result for result in db.db_results):
        item = (ip, port) # ,proxyType )
        db.add_AP(config.DATABASE, item)
db.get_all(config.DATABASE)
print(len(db.db_results), "Proxies in database")

