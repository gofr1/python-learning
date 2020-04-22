#!/usr/bin/env python3

import urllib.request as ur
import json, textwrap

def main():
    with ur.urlopen("https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224") as f:
        text = f.read()
        decodedText = text.decode("utf-8")
        print(textwrap.fill(decodedText, width=50))
    
    print(50*"-")

    obj = json.loads(decodedText)
    title = obj['items'][0]['volumeInfo']['title']
    author = obj['items'][0]['volumeInfo']['authors'][0]
    subtitle = obj['items'][0]['volumeInfo']['subtitle']

    print(f'{subtitle} by {author} "{title}"')

if __name__ == '__main__':
    main()