#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://scrapingclub.com/exercise/list_basic/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    # to go through all pages
    pages = soup.find('ul', class_='pagination')
    links = pages.find_all('a', class_='page-link')

    urls = [''] # with empty string we will get current page 
    cnt = 1

    for link in links:
        pageNum = int(link.text) if link.text.isdigit() else None
        if pageNum != None:
            x = link.get('href')
            urls.append(x)
    
    for u in urls:
        newUrl = url + u
        response = requests.get(newUrl)
        soup = BeautifulSoup(response.text, 'lxml')

        # get all items on page
        items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    
        for item in items:
            itemName = item.find('h4', class_='card-title').text
            itemPrice = item.find('h5').text
        
            print(f'{cnt} ) Price: {itemPrice}, Item Name: {itemName.strip()}')
            cnt += 1


if __name__ == '__main__':
    main()