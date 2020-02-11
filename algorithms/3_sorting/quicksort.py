# implement a quicksort

items = [20, 6, 8, 53, 56, 23, 87, 41, 49, 19]

def quicksort(dataset, first, last):
    if first < last:
        # calculate the split point
        pivot_idx = partition(dataset, first, last)

        # now sort the two partitions
        quicksort(dataset, first, pivot_idx - 1)
        quicksort(dataset, pivot_idx + 1, last)

def partition(datavalues, first, last):
    # choose the first item as the pivot value
    pivot_value = datavalues[first]
    # establish the upper and lower index
    lower = first + 1
    upper = last
    # start searching for the crossing point
    done = False
    while not done:
        # advance the lower index
        while lower <= upper and datavalues[lower] <= pivot_value:
            lower += 1
        # advance the upper index
        while upper >= lower and datavalues[upper] >= pivot_value:
            upper -= 1
        # if the two indexes cross, we have found the split point
        if upper <= lower:
            done = True
        else:
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp

    # when the split point is found, exchange the pivot value
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp

    # return the split point index
    return upper

# test
print("Before: ", items)
quicksort(items, 0, len(items) - 1)
print("After: ", items)