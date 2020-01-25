for letter in ['c','a','t']:
    print(letter)

print(letter) # will print t, variable is not cleared after cicle
# but if 'for' is used in function - it would be removed

# bad practice
animals = ['cat', 'dog', 'bird']
for index in range(len(animals)):
    print(index, animals[index])
# good practice
animals = ['cat', 'dog', 'bird']
for index, value in enumerate(animals):
    print(index, value)

# interaption
numbers = [3, 5, 9, -1, 3, 1]
result = 0
for item in numbers:
    if item < 0:
        break
    result += item # same is result = result + item
print(result)

# skip elements
numbers = [3, 5, 9, -1, 3, 1]
result = 0
for item in numbers:
    if item < 0:
        continue # if <0 then we dont use item, but continue with next variavle
    result += item # same is result = result + item
print(result)

# 'in' also is used to check if some element is in list

animals = ['cat', 'dog', 'bird']
'bird' in animals

# removing from list with 'for'
dinos = ['raptor', 't-rex', 'compsognatus', 'triceratops']
for dino in dinos:
    if dino not in ['raptor', 't-rex']:
        dinos.remove(dino)
print(dinos)
# ['raptor', 't-rex', 'triceratops']
# because 'compsognatus' is removed and now element with index = 3 'triceratops'
# became second, so cicle is stopped

# solution1
dinos = ['raptor', 't-rex', 'compsognatus', 'triceratops']
dinos_to_remove = []
for dino in dinos:
    if dino not in ['raptor', 't-rex']:
        dinos_to_remove.append(dino)
for dino in dinos_to_remove:
    dinos.remove(dino)
print(dinos)

# solution2
dinos = ['raptor', 't-rex', 'compsognatus', 'triceratops']
for dino in dinos[:]: # copy of dinos
    if dino not in ['raptor', 't-rex']:
        dinos.remove(dino)
print(dinos)

# else
positive = False
numbers = [3, 5, 9, 1, 3, 1]
for num in numbers:
    if num < 0:
        break
else: # 'else' would be launched if 'for' didn't get to 'break' 
    positive = True
print(positive)

# while 
# is used when you don't have basic access to object that can be used for iteration

# counter
n = 3
while n > 0:
    print(n)
    n -= 1 # same as n = n - 1

# break - to exit the while loop
n = 3
while True:
    print(n)
    n -= 1
    if n == 0:
        break

# task1

names = ['Maria', 'Pavel', 'Sergey', 'Artur', 'Oksana', 'Alexander']
l = 0
c = 0
for name in names:
    l += len(name)
    c += 1
print('Avg:', l/c)

# task2
names = ['Maria', 'Pavel', 'Sergey', 'Artur', 'John', 'Oksana', 'Alexander']
for name in names:
    if name == 'John':
        print('Found him! :)')
        break
else:
    print('John not found :(')