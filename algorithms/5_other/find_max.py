# use a recursive algorithm to find a maximum value

# declare a list of items to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_max(items):
    # breaking condition: last item in list? return it
    if len(items) == 1:
        return items[0]
    
    # otherwise get the first item and call function
    # again to operateon the rest of the list
    op1 = items[0]
    op2 = find_max(items[1:])

    # perform the comparison when we're down to just two
    if op1 > op2:
        return op1
    else:
        return op2

def find_max1(items):
    max_val = items[0]
    for i in range(1, len(items)):
        max_val = items[i] if max_val <= items[i] else max_val
    return max_val


# test
print(find_max(items))
print(find_max1(items))