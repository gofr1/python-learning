# 4
import requests
from bs4 import BeautifulSoup

# pattern is 'and the next nothing is 44827'
# function to get next nothing urls
def url_loop(incoming_url):
    # create new url based on main_url
    url = main_url + incoming_url
    text_from_url = requests.get(url).text[:]
    nothing = text_from_url.split(' ')

    # after spliiting the response text take length of list
    nothing_len = len(nothing)
    
    if nothing_len < 5:
        return None, None, text_from_url

    # this element we will return with new url
    nothing_num = nothing[nothing_len-1]

    # populate new url
    next_url = '{}?{}={}'.format(linkedlist_url, nothing[nothing_len-3], nothing_num)
    return next_url, nothing_num, text_from_url

def get_results(row_num, nothing_num):
    print('{0:>3} {1}'.format(row_num, nothing_num))

# number of tries
num_tries = 400

# get the data of main page of the task 4
main_url = 'http://www.pythonchallenge.com/pc/def/'
linkedlist_url = 'linkedlist.php'
url = main_url + linkedlist_url
content = requests.get(url).text[:]

# get the first link from <a href="link" />
parsed_html = BeautifulSoup(content)
first_url = parsed_html.a['href']
next_url = first_url

# create dict and paste first result in it
all_nothings = dict()
all_nothings[0] = first_url.split('=')[1]
start_from = 1
a = 0

# and all the next 
for i in range(start_from, num_tries):
    try:
        next_url, num, message_text = url_loop(next_url)
        a = int(num)
    except (ValueError, TypeError):
        print('Script stoped at i = {}, last_num was {}. We get this message: {}.\n '.format(i, all_nothings[i-1], message_text))
        if message_text == 'Yes. Divide by two and keep going.':
            next_url = linkedlist_url + '?nothing=' + str(int(int(all_nothings[i-1])/2))
            continue
        elif message_text.find('html') > 0:
            print(message_text)
            break
        else:
            break
    else:
        all_nothings[i] = num
