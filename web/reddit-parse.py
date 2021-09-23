#!/usr/bin/env python3

from lxml import html
import requests

# Enter text to search
search_for = 'windows'

# Defining base url 
base_url = 'https://www.reddit.com'

# Getting page content
page = requests.get(f'{base_url}/search/?q={search_for}')
  
# Parsing the page
tree = html.fromstring(page.content)
  
# Get title of the page using XPath
titles = tree.xpath('//title')
for title in titles:
    print(title.text_content())

# Get all links & link titles using XPath
links = tree.xpath('//div/a[@data-click-id="body"]/@href')
texts = tree.xpath('//div/a[@data-click-id="body"]/div/h3/span')

# Merging both objects
search_results = zip(links, texts)

# Printing out first 10 results
i = 1
for link, text in search_results:
    if i <= 10:
        print(f'{i}. {text.text_content()}')
        print(f'{base_url}{link}')
    i += 1
    