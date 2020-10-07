#10
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup

def look_and_say(strt, tms):
    '''Implementation of Look-and-say sequence
        1 is read off as "one 1" or 11.
        11 is read off as "two 1s" or 21.
        21 is read off as "one 2, then one 1" or 1211.
        1211 is read off as "one 1, one 2, then two 1s" or 111221.
        111221 is read off as "three 1s, two 2s, then one 1" or 312211.
    '''
    if tms == 0:
        return strt
    cnt = ''
    cur = strt[0]
    result = ''
    for i in strt:
        if i != cur:
            result += str(len(cnt)) + str(cur)
            cnt = ''
        cnt += i
        cur = i
    result += str(len(cnt)) + str(cur)
    tms -= 1
    if tms > 0:
        return look_and_say(result, tms)
    else:
        return result

standard_url = "http://www.pythonchallenge.com/pc/return/"

url = f"{standard_url}bull.html"
response = requests.get(url, auth = HTTPBasicAuth('huge', 'file'))
page_contents = BeautifulSoup(response.text, 'html.parser')
contents = page_contents.find_all('area')[0].get('href')
main = page_contents.find_all('font')[0].string

url = f"{standard_url}{contents}"
response = requests.get(url, auth = HTTPBasicAuth('huge', 'file'))
page_contents = BeautifulSoup(response.text, 'html.parser')

print(f'You need to solve: {main} equation using this list: {page_contents}')
print('And the answer is: {0}'.format(len(look_and_say('1', 30))))
