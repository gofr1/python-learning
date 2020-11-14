#!/usr/bin/env python3

import requests, json

url = 'https://api.exchangeratesapi.io/latest?base=EUR'

responce = requests.get(url)

content = responce.content
rate = json.loads(content)

print(f"{rate['date']}: 1 EUR = {rate['rates']['RUB']} RUB = {rate['rates']['CZK']} CZK")