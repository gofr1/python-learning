# linked list example

# node
# stores value and next element
class Node(object):
    def __init__ (self, val):
        self.val = val
        self.next = None
    
    def get_data(self):
        return self.val
    
    def set_data(self, val):
        self.val = val
    
    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next

# linked list
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0
    
    def get_count(self):
        return self.count
    
    def insert(self, data): # insert in the beggining only
        new_node = Node(data) # so we are moving the haed
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, val):
        item = self.head
        while (item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()
        return None
    
    def deleteAt (self, idx):
        if idx > self.count:
            return 
        if idx == 0:
            self.head = self.head.get_next()
        else:
            temp_idx = 0
            node = self.head
            while temp_idx < idx - 1:
                node = node.get_next()
                temp_idx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1
    
    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()

    def dump_list_with_next(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data(), ' next node is: ', tempnode.get_next().get_data() if tempnode.get_next() != None else None)
            tempnode = tempnode.get_next()
# example

item_list = LinkedList()
item_list.insert(38)
item_list.insert(49)
item_list.insert(13)
item_list.insert(15)
item_list.dump_list()
  
print("Item count: ", item_list.get_count())
print("Finding item: ", item_list.find(13))
print("Finding item: ", item_list.find(78))

item_list.deleteAt(3)
print("Item count: ", item_list.get_count())
print("Finding item: ", item_list.find(38))
item_list.dump_list()

item_list.dump_list_with_next()
