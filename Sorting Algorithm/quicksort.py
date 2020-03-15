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


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index
# 10 80 30 70 40 50 90


#Fnction to do Quick sort
def quickSort(arr, low, high):
    if low < high:

        #  pi is partitioning index, arr[p] is now
        # at right place
        pi = partition2(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# Test code
arr = [10, 7, 8, 9, 1, 5, 4, 6]
# arr = [10, 7, 8]
n = len(arr)
quickSort(arr, 0, n -1)
print("Sorted array is: ", end = "")
print(arr)


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