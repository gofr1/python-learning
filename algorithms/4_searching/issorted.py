# determine if the list is sorted

items1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
items2 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

def is_sorted (item_list):
    # using the brute force method
    for i in range(0, len(item_list) - 1):
        if item_list[i] > item_list[i+1]:
            return False
    return True

print(is_sorted(items1))
print(is_sorted(items2))

def is_sorted1(item_list):
    return all(item_list[i] <= item_list[i+1] for i in range(0, len(item_list) - 1))

print(is_sorted1(items1))
print(is_sorted1(items2))