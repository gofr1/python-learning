# searching for an item in an unordered list
# sometimes is called a Linear search

items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_item(item, item_list):
    for i in range(0, len(item_list)):
        if item == item_list[i]:
            return i

print(find_item(87, items))
print(find_item(250, items))