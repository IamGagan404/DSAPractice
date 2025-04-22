# Sorting
# Bubble Sort
def bubbleS_sort(arr):  # O(n^2) O(1)
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Insertion sort
def insertion_sort(arr):  # O(n^2) O(1)
    n = len(arr)
    for i in range(1, n):
        j = i - 1
        while j >= 0 and arr[i] < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = arr[i]
    return arr
# Merge Sort
def merge_sort(arr): # O(nlogn) O(n)  This can be in-place way also
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)
def merge(left,right):
    merged = [None] * (len(right)+len(left))
    i,j,k = 0,0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged[k] = left[i]
            i += 1
        else:
            merged[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        merged[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        merged[k] = right[j]
        j += 1
        k += 1
    return merged


print(merge_sort([2,3,1,41,3,78]))

# Selection Sort O(n^2)
# get max element put it at end in next iteration reduce array by 1 from last

# Quick Sort
# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot


# Function to find the partition position
def partition(array, low, high):

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1

# function to perform quicksort

arr.sort()
def quickSort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)


data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)




# Timsort
# Merge sort plus insertion sort(works great with partially sorted arrays)
# #


