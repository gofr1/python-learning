# highly optimized built-in type in python
# key-value structure

info = {'first': 'Pete', 'last': 'Best'}

info = dict([('first', 'Pete'), ('last', 'Best')])

info = dict(first = 'Pete', last = 'Best')

# append
info['age'] = 20
info['occupation'] = 'Drummer'

print(info)
print(info['age'])

# dictionaries don't copy data
# if you put variable in dictionary it will create a link to it
# and increase variable use counter by 1

# if you try to get value of key that is not in dictionary you
# will get KeyError

# 'in' is also used with dictionaries
print('band' in info)
print('first' in info)

# to bypass KeyValue error you can use get mrthod

genre = info.get('genre', 'rock') # dict.get(key, default = None)
print(genre) # if key is not in dictionary it will show default value
# that was provided

# setdefault
# is like get() but will set dict[key] = default
# if this key is not in dict

print(info)
info.setdefault('genre', 'rock')
print(info)

# can be used for key counter

names = ['Kurt', 'Dave', 'Chris', 'Kurt']
count = {}
for name in names:
    count.setdefault(name, 0)
    count[name] += 1
print(count)

# same, but without setdefault()
names = ['Kurt', 'Dave', 'Chris', 'Kurt']
count = {}
for name in names:
    if name not in count:
        count[name] = 1
    else:
        count[name] += 1
print(count)

# also for counting we can use collections.Counter class

import collections
count = collections.Counter(['Kurt', 'Dave', 'Chris', 'Kurt'])
print(count)
print(count['Kurt'])

# example

band1_names = ['Kurt', 'Dave', 'Chris']
band2_names = ['Dave']
names_to_bands = {}
for name in band1_names:
    names_to_bands.setdefault(name, []).append('Nirvana')
for name in band2_names:
    names_to_bands.setdefault(name, []).append('Dave Matthews Band')
print(names_to_bands)
#  {'Kurt': ['Nirvana'], 'Dave': ['Nirvana', 'Dave Matthews Band'], 'Chris': ['Nirvana']}
print(type(names_to_bands))

# same example with defaultdict
from collections import defaultdict
names_to_bands = defaultdict(list)
for name in band1_names:
    names_to_bands[name].\
        append('Nirvana')
for name in band2_names:
    names_to_bands[name].\
        append('Dave Matthews Band')
print(names_to_bands)
print(type(names_to_bands))

# deleting keys
del names_to_bands['Chris']
print(names_to_bands)

# you must not go through dict and delete values
# it would delete some record from dict and raise RuntimeError
# example
data = {'name': 'Ilia'}
for key in data:
    del data[key]
print(data)

# if you loop through dict via for it will show keys by default
data = {'Adam': 2, 'Zeek': 5, 'Fred': 3}
for name in data:
    print(name)
# or
for name in data.keys():
    print(name)

# and for values use self-titled method
for name in data.values():
    print(name)

# also we can use items for both
for key, value in data.items():
    print(key, value)

# {'Adam': 2, 'Zeek': 5, 'Fred': 3} from dict
list(data.items())
# [('Adam', 2), ('Zeek', 5), ('Fred', 3)] to list of tuples

# sort
for name in sorted(data.keys()): # ascending
    print(name)
for name in sorted(data.keys(), reverse= True): # descending
    print(name)

# keys should be able to hash


# task1
info = {'first': 'Ilia', 'last': 'Odintsov', 'age': '35'}
print(type(info))

# task2
phone = dict(model= 'Nokia 3.1 plus',\
    os ='Android 9 Pie',\
    weight = '180g',\
    display_size = '6inches'\
)

# task3 and task4
import re
lorem = """
To speak truly, few adult persons can see nature. Most persons do not see the sun. At least they have a very superficial seeing. The sun illuminates only the eye of the man, but shines into the eye and the heart of the child. The lover of nature is he whose inward and outward senses are still truly adjusted to each other; who has retained the spirit of infancy even into the era of manhood. His intercourse with heaven and earth, becomes part of his daily food. In the presence of nature, a wild delight runs through the man, in spite of real sorrows. Nature says,—he is my creature, and maugre all his impertinent griefs, he shall be glad with me. Not the sun or the summer alone, but every hour and season yields its tribute of delight; for every hour and change corresponds to and authorizes a different state of the mind, from breathless noon to grimmest midnight. Nature is a setting that fits equally well a comic or a mourning piece. In good health, the air is a cordial of incredible virtue. Crossing a bare common, in snow puddles, at twilight, under a clouded sky, without having in my thoughts any occurrence of special good fortune, I have enjoyed a perfect exhilaration. I am glad to the brink of fear. In the woods too, a man casts off his years, as the snake his slough, and at what period soever of life, is always a child. In the woods, is perpetual youth. Within these plantations of God, a decorum and sanctity reign, a perennial festival is dressed, and the guest sees not how he should tire of them in a thousand years. In the woods, we return to reason and faith. There I feel that nothing can befall me in life,—no disgrace, no calamity, (leaving me my eyes,) which nature cannot repair. Standing on the bare ground,—my head bathed by the blithe air, and uplifted into infinite space,—all mean egotism vanishes. I become a transparent eye-ball; I am nothing; I see all; the currents of the Universal Being circulate through me; I am part or particle of God. The name of the nearest friend sounds then foreign and accidental: to be brothers, to be acquaintances,—master or servant, is then a trifle and a disturbance. I am the lover of uncontained and immortal beauty. In the wilderness, I find something more dear and connate than in streets or villages. In the tranquil landscape, and especially in the distant line of the horizon, man beholds somewhat as beautiful as his own nature.
"""

lorem_words = re.split('\. |; |, |\n| ', lorem.lower())
words_count = {}
for word in lorem_words:
    insert_word = word
    words_count.setdefault(insert_word, 0)
    words_count[insert_word] += 1
print(words_count)

# task5
words = list(lorem_words)
anagramms = {}
for word in words:
    for another_word in words[:]:
        if sorted(list(word)) == sorted(list(another_word)) and word != another_word:
            anagramms.setdefault(word, []).append(another_word)
            words.remove(another_word)
print(anagramms)

# task6
# page rank
links = [('a', 'b'), ('a', 'c'), ('b', 'c')]
ranked_links = {}
links_count = {}
for link in links:
    ranked_links.setdefault(link[0], 1)
    ranked_links.setdefault(link[1], 1)

for key, value in ranked_links.items():
    for link in links:
        if key in link[0]:
            links_count.setdefault(link[0], 0)
            links_count[link[0]] += 1
            
iterations = 10
while iterations > 0:
    for key, value in ranked_links.items():
        links_count.setdefault(key, 0)
        cnt = links_count[key]
        if cnt != 0:
            rating = value/cnt
            for link in links:
                if key in link[0]:
                    ranked_links[link[1]] += rating
                    ranked_links[link[1]] *= 0.85
    iterations -= 1

print(ranked_links)

