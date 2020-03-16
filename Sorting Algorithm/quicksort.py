def partition(arr, low, high):
    i = low - 1 # index of smaller element

    pivot = arr[high]  #  pivot

    for j in range(low, high):

        # If current element is smaller than the pivot
        if arr[j] < pivot:
            # increment index of smaller element
            i  = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i+1]
    return (i + 1)

def partition2(arr, low, high):
    i = low - 1 # index of smaller element
    middle = (low + high) // 2
    pivot = arr[middle]  #  pivot
    arr[middle], arr[high] = arr[high], arr[middle]

    for j in range(low, high):

        # If current element is smaller than the pivot
        if arr[j] < pivot:
            # increment index of smaller element
            i  = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i+1]
    return (i + 1)


def partition3(arr, low, high):

    middle = (low + high) // 2
    pivot = arr[middle]  #  pivot
    

    left = low
    right = high
    l = len(arr)

    while left < right:
        while left < l and arr[left] < pivot:
            left += 1
        while right >= 0 and arr[right]  > pivot:
            right -= 1
        
        arr[left], arr[right] = arr[right], arr[left]

    return middle

def partition4(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        
        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1
        
        while low <= high and array[high] >= pivot:
            high = high - 1

        

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high

def partition5(array, left, right):
    pivot = array[(left + right) // 2]
    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right]  > pivot:
            right -= 1

        if left <= right :
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    return left

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index
# 10 80 30 70 40 50 90
"""
9 7 3
"""

#Fnction to do Quick sort
def quickSort(arr, low, high):
    if low < high:

        #  pi is partitioning index, arr[p] is now
        # at right place
        pi = partition5(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi - 1, high)

def quickSort1(arr, low, high):
    if low < high:


        pi = partition5(arr, low, high)
        quickSort1(arr, low, pi - 1)
        quickSort1(arr, pi, high)


def quickSort2(array, left, right):
    if  left >= right:
        return
    
    index = partition5(array, left, right)
    quickSort2(array, left, index - 1)
    quickSort2(array, index, right)


# Test code
arr = [10, 7, 8, 9, 1, 5, 4, 6]
# arr = [10, 7, 8]
n = len(arr)
quickSort1(arr, 0, n -1)
print("Sorted array is: ", end = "")
print(arr)


# arr = [1, 7, 8, 1, 10]
# partition5(arr, 0, len(arr) - 1)
# print(arr, len(arr) // 2)

# Analysis of QuciSort
"""
Time taken by QuickSort in general can be written as following
T(n) = T(k) + T(n - k - 1) + O(n)
The first two terms are for two recursive calls, the last term is for the partition process.
k is the number of elements which are smaller than pivot.
The time taken by QuickSort depends upon the input array and partition straregy.
Following are three cases.
Worst Case:
The worst case occurs when the partition process always picks greatest or smallest element as pivot.
If we consider above partition strategy where last element is always picks as pivot, the worst case would occur
when the array is already sorted in increasing or decreasing order. Following is recurrence for worst case.
T(n) = T(0) + T(n - 1) + O(n)
which is equivalent to 
T(n) + T(n - 1) + O(n)
the solution of above recurrence is O(n^2).

Best Case: The best case occurs when the partition process always picks the middle element as  pivot. Following is recurrence for best case.
T(n) = 2T(N/2) + O(n)
The solution of above recurrence is O(nLogn). it can be solved using case 2 of Master Theorem.

Average case:
To do average case analysis, we need to consider all possible permutation of array and calculate time taken by every permutation which dowsn't look east.
We can get an idea of average case by considering the case when partiotion puts O9n/9) elements in one set and O(9n/10) elements in other set. Following is recurrence for this case.
T(n) = T(n/9) + T(9n/10) + O(n)
Solution of aboce recurrence is also O(nLogn)

Although the worst case time complexity of QuickSort is O(n^2) which is more than many other sorting algorithms like Merge Sort and Heap Sort,
QuickSort is faster in pratice, because its inner loop can be efficiently implrmented on most architectures, and in most real-world data.
QuickSort can be implemented in different ways by changing the choice of pivot, so that the worst case rarely occurs for a given type of data. However, merge sort is generally considered better when data is huge and stoed in external storage.
"""