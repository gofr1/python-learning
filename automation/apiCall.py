#!/usr/bin/env python3

import requests, json

baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc': '9780441172719'} # or 9780439023528

responce = requests.get(baseUrl,params=parameters)

content = responce.content # get content
info = json.loads(content) # make a dict from json

# now lets work w/dict
print(f"title: {info['items'][0]['title']}")

