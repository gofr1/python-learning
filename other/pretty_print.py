import pprint

# Better with nested dicts
my_dict = {'name': 'John', 'age': '26', 'personality': 'awesome', 'info': {'skills': ['python', 'sql', 'big data'], 'level': 'senior'}}

print(my_dict)
#* {'name': 'John', 'age': '26', 'personality': 'awesome', 'info': {'skills': ['python', 'sql', 'big data'], 'level': 'senior'}}

pp = pprint.PrettyPrinter(indent=2, width=20, compact=True)
pp.pprint(my_dict)
#* { 'age': '26',
#*   'info': { 'level': 'senior',
#*             'skills': [ 'python',
#*                         'sql',
#*                         'big '
#*                         'data']},
#*   'name': 'John',
#*   'personality': 'awesome'}