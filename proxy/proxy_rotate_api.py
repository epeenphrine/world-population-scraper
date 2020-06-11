
#pip install libraries
import bs4
import time
import json
import random
import requests
import bs4 as bs
import os

from .proxy_scrape import scrape

def proxy_rotate_api(url):
    # json file check
    def json_load():
        with open("proxydictlist.json") as f:
            print("json file exists")
            proxies_list = json.load(f)
            return proxies_list

    def json_create():
        with open("proxydictlist.json", "w") as f:
            json.dump([], f)
            return

    if os.path.exists("proxydictlist.json"):
        proxies_list = json_load()
    else:
        print("json file doesn't exist creating json file ...")
        json_create()
        proxies_list = json_load()

    print(f"attempting to connect to: {url}")
    print(len(proxies_list))

    headers_list = [
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; x64; fr; rv:1.9.2.13) Gecko/20101203 Firebird/3.6.13',
        'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
        'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
        'Mozilla/5.0 (Windows NT 5.2; RW; rv:7.0a1) Gecko/20091211 SeaMonkey/9.23a1pre'
    ]
    # check if proxies_list is empty or not
    if proxies_list and (len(proxies_list) >= 50):
        for i in range(0, len(proxies_list)):
            try:
                #pick random proxy and header
                proxy_pick = random.choice(proxies_list)
                headers_pick = {
                "User-Agent" : random.choice(headers_list)
                }
                # requests
                res = requests.get(url, headers=headers_pick, proxies=proxy_pick, timeout=(1))
                if res:
                    json_data = json.loads(res.content)
                    print("got json")
                    return json_data 

            except:
                # proxies that do not work are removed from the list and json
                print(f"{proxy_pick} did not work")
                
                proxies_list.remove(proxy_pick)
                with open('proxydictlist.json', 'w') as f:
                    json.dump(proxies_list, f)

                print(f"{proxy_pick} removed")
                print(len(proxies_list))
    # start scrape to get new proxies and start function again
    else:
        scrape()
        return proxy_rotate_api(url)