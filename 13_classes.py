# every object has a type
# it is a class of an object
# class has methods

class Chair: # class is defined
    ''' A Chair on a chairlift ''' # comment ot what this class is for
    max_occupants = 4 # class attribute
    # it used to store state that is common for all instance of the class

    # methods are defined now
    def __init__(self, id): # construcor (__init__) initiates a state of instance
        self.id = id # self is an instance of a class
        self.count = 0 # and it stores current state of instance
    
    def load(self, number): # some methods
        self.count += number
    
    def unload(self, number):
        self.count -= number

dir(Chair) # show all methods and attributes
Chair.max_occupants # 4

Chair.__class__ # <class 'type'>
Chair.max_occupants.__class__ # <class 'int'>
Chair.load.__class__ # <class 'function'>

help(Chair)
# class Chair(builtins.object)
# |  Chair(id)
# |  
# |  A Chair on a chairlift
# |  
# |  Methods defined here:
# |  
# |  __init__(self, id)
# |      Initialize self.  See help(type(self)) for accurate signature.
# |  
# |  load(self, number)
# |  
# |  unload(self, number)
# etc
# |  ----------------------------------------------------------------------
# |  Data and other attributes defined here:
# |  
# |  max_occupants = 4

chair = Chair(21) # now chair variable points on object (instance)
# it doesn't point on class
# this object refers to class Chair

# reference to attributes
chair.count # 0
chair.id # 21

# at first python looks into instance for attributes
# then it goes to class
chair.max_occupants # 4
# if there is no attribute python throws AttributeError

# method call
chair.load(3) # this method is not in an instance
# because only id and count are in __init__ part
# so python finds this method in class
# it is same as Chair.load(chair, 3)

#Current state of an instance is stored in __dict__ attribute:
chair.__dict__
# {'id': 21, 'count': 3}

# private methods
# they starts from _ (The symbol underscore ( _ ), 
# also called underline, underdash, low line, or low dash)

class CorrectChair: 
    ''' A Chair on a chairlift '''
    max_occupants = 4

    def __init__(self, id):
        self.id = id
        self.count = 0
    
    def load(self, number):
        new_val = self._check(self.count + number)
        self.count = new_val
    
    def unload(self, number):
        new_val = self._check(self.count - number)
        self.count = new_val
    
    def _check(self, number): # private method is defined
        if number < 0 or number > self.max_occupants:
            raise ValueError('Invalid count:{}'.format(number))
        return number

# only instances of a class can access private methods
# f.e. load and unload methods can call _check


# task3

import random

class TweetGenerator:
    max_length = 280

    def __init__(self, id, author, content):
        self.id = id
        self.content = content
        self.likes = 0
        self.author = author
    
    def post_tw(self, tweet):
        checked_tweet = self._check_tw(tweet)
        self.content = checked_tweet
    
    def like_tw(self, likes):
        self.likes += likes

    def _check_tw(self, tweet):
        if len(tweet) > self.max_length:
            raise ValueError('Tweet is too long: {} symbols from {} available.'.format(len(tweet), self.max_length))
        return tweet

some_tweets = [
("I'm about as intimidating as a butterfly.", "Dan Howell"),
("What do you want? Where's the goddamn ice I ordered? Where's the booze? \
There's a war on, man! People are being killed!", "Hunter S. Thompson"),
("What's my age again?", "Blink-182"),
("Some quotations,' said Zellaby, 'are greatly improved by lack of context.", "John Wyndham"),
("It looks rather ordinary,' said the Snork. 'Unless you consider that a top hat \
is always somewhat extraordinary, of course.", "Tove Jansson"),
("I said 'I'm sorry, sir, but we don't speak Swedish.' Well, of course you don't. \
Neither do I. Who the hell speaks Swedish?", "John Green"),
("Tried to escape, to block out the fact that I was being eaten alive by arachnids. \
For some reason the only thing I could replace it with was the image of being eaten by tiny clowns.", "David Wong")
]
posted_tweets = []

for i in range(len(some_tweets)):
    posted_tweets.append(TweetGenerator(i,some_tweets[i][1],some_tweets[i][0]))

for post in posted_tweets:
    post.like_tw(random.randint(0,100))
    print('Tweet: {}\nAuthor: {}\nLikes: {}\n'.format(post.content, post.author, post.likes))
