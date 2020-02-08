# for queue lets use deck

from collections import deque

# create empty queue
queue = deque()

# add some items to queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# print queue contents
print(queue)

# pop an item off the front of the queue
x = queue.popleft()
print(x)
print(queue)