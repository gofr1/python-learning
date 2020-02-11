# searching for an item in an ordered list
# this technique uses binary search

items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

def binary_search (item, item_list):
    # get the list size
    list_size = len(item_list) - 1
    # start at the two ends of the list
    lower_idx = 0
    upper_idx = list_size

    while lower_idx <= upper_idx:
        # calculate the middle point
        mid_point = (lower_idx + upper_idx) // 2

        # if item is found, return the index
        if item_list[mid_point] == item:
            return mid_point
        
        # otherwise get the next midpoint
        if item > item_list[mid_point]:
            lower_idx = mid_point + 1
        else:
            upper_idx = mid_point - 1

    if lower_idx > upper_idx:
        return None

print(binary_search(23, items))
print(binary_search(87, items))
print(binary_search(250, items))
