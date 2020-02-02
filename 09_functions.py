def add_2 (num): # def means define
    '''
    return 2 more than num
    '''
    result = num + 2
    return result # if no return specified returnes None

print(add_2(4))

# python creates new object function, then saves it's id in variable with 
# name of function

# when function is executed python check variables:
# 1. local - vars that are defined within func
# 2. global
# 3. built-in

x = 2 # global
def scope_demo():
    y = 4 # local (will be removed after execution of function)
    print("Local: {}".format(y))
    print("Global: {}".format(x))
    print("Built-in: {}".format(dir))

scope_demo()

# python has built-in functions locals and globals:

y = 2
print(globals())
def foo():
    x = 1
    print(locals())

foo()

# multi-parameters

def add_two_nums(a, b):
    return a + b

add_two_nums(4, 6)
add_two_nums(4.0, 6.0)
add_two_nums('4', '6')
add_two_nums(4, 6.0) # float
add_two_nums(4, '6') # TypeError

# default parameters

def add_n (num, n=3): # default params are always put after basic (non-default) params
    '''default to adding 3''' # in other way we will get SyntaxError
    return num + n

add_n(2)
add_n(15,-5)

# don't use lists and dictionaries (mutable) as default parameters
# because def parameters are created one time when function is defined
# and the same object will be used

def to_list(value, default=[]):
    default.append(value)
    return default

to_list(4) # [4]
to_list('hello') # [4, 'hello']

# we can use None for default parameters of mutable types

def to_list2(value, default=None):
    if default is None:
        default = []
    # or in one string:
    # default = default if default is None else []
    default.append(value)
    return default

to_list2(4) # [4]
to_list2('hello') # ['hello']

# function name convention
# 1. lower case
# 2. words separated by _
# 3. don't start with numbers
# 4. don't redefine built-ins
# 5. don't use key-words

# task1

def is_odd(num):
    return True if num%2 == 0 else False

is_odd(3)
is_odd(10)
is_odd(5.0)
is_odd(4.0)

# task2

def is_prime(num):
    modulo_count = {}
    if num < 1 or type(num) != int:
        return False
    else:
        for number in range(1, num+1, 1):
            modulo_count.setdefault(num%number, 0)
            modulo_count[num%number] +=1
        if modulo_count[0] > 2:
            return False
        else:
            return True

is_prime(41)
is_prime(237)

# task3

def binary_search(input_set, search_value):
    search_index = -1
    for index in range(len(input_set)):
        if search_value == input_set[index]:
            search_index = index
    return search_index

some_set = ['Maria', 'Pavel', 'Sergey', 'Artur', 'Oksana', 'Alexander']
binary_search(some_set, 'Artur')


# task4
camel_string = 'ThisIsCamelString'

def make_it_not_camel (camel_string, separator='_'):
    new_string = ''
    for letter in camel_string:
        new_string += separator + letter.lower() if letter == letter.capitalize() else letter.lower()
    return new_string[1:]

make_it_not_camel(camel_string)
make_it_not_camel(camel_string, '-')