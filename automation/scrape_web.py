#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def main():
    url = 'http://quotes.toscrape.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)

    # all quotes are in tag span class=text 
    quotes = soup.find_all('span', class_='text')

    # all authors are in small tag class=author
    authors = soup.find_all('small', class_='author')
    
    # let's add tags
    tags = soup.find_all('div', class_='tags')

    for quote, author, tags_ in zip(quotes, authors, tags):
        print(quote.text, author.text)
        for tag in tags_.find_all('a', class_='tag'):
            print(tag.text, end=' ')
        print()
    
if __name__ == '__main__':
    main()