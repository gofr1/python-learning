from tkinter import Tk, Text, VERTICAL
from tkinter import ttk

import requests
from bs4 import BeautifulSoup

url = 'https://www.lipsum.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
lorem = soup.find_all('p')

root = Tk()
text = Text(root, width=40, height=10, wrap='word')
text.grid(row=0, column=0)
text.insert('1.0', f'{lorem[5].text}\n{lorem[6].text}')

# add a scroll bar
scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=text.yview)
scrollbar.grid(row=0, column=1, sticky='ns')

# to make scroll bar reference the place in text
text.config(yscrollcommand=scrollbar.set)