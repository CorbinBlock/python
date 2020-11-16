#!/usr/bin/env 
#python3.7
import requests
with requests.Sessions() as s:
    url = "https://www.ozk.com/personal/"
    r = s.get(url)
    print(r.content)
