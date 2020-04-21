#!/usr/bin/env python3

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start tag: {tag}")
        for attr in attrs:
            print(f"Attribute: {attr}")
    
    def handle_endtag(self, tag):
        print(f"End tag: {tag}")
    
    def handle_comment(self, data):
        print(f"Comment: {data}")
    
    def handle_data(self, data):
        print(f"Data: {data}")

def main():
    parser = MyHTMLParser()
    parser.feed("<html><head><title>Coder</title></head><body><h1><!--hi-->Python is great!</h1></body></html>")
    print()
    
if __name__ == '__main__':
    main()