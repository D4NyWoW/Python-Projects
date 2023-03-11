def bubble_sort(array):
    n = len(array)

    for i in range(n):
        already_sorted = True
        # looking at each item of the list one by one, comparing it with its adjacent value
        # with each iteration, the portion of the array that you look at shrinks because the remaining items have already been sorted.
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # if the item is greater than it's adjacent value, then swap
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
            # if there were no swaps during the last iteration, the array is already sorted, and you can terminate
        if already_sorted:
            break
    
    return array


print(bubble_sort([8,2,6,4,5]))