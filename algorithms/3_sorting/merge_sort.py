items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def merge_sort(dataset):
    if (len(dataset)) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]
        # recursively break down the arrays
        merge_sort(leftarr)
        merge_sort(rightarr)
        # now perform the merging
        i = 0 # index into the left array
        j = 0 # index into the right array
        k = 0 # index into the merged array
        # while both arrays have content
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1
        # if left array still has values
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1
        # if right array still has values
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1       

# test
print("Before: ", items)
merge_sort(items)
print("After: ", items)