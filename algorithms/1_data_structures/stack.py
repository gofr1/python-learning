# in python simple list will be used as stack

# create an empty stack
stack = []

# push item onto the stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

# print the stack contents
print(stack)

# pop an item off the stack
x = stack.pop() # actualy I could give an index, bur lets KISS
print(x)
print(stack)