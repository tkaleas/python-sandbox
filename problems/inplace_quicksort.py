# IN PLACE QUICKSORT SOLUTION
## ERRORS: indices an issue, double check and create most simple version
#   make sure to account for pivot swapping for partition function

def partition(arr, pivot, lo, hi):
    pivot = arr[lo]
    j = hi
    i = lo + 1

    while  i <= j :
        if arr[i] < pivot:
            i += 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1

    #swap pivot to correct position
    array[lo], array[i - 1] = array[i - 1], array[lo]
    return i - 1

def inPlayQuickSortHelper(arr, lo, hi):
    
    if lo >= hi:
        return

    pivot = arr[lo]
    i = partition(arr, pivot, lo, hi)

    inPlayQuickSortHelper(arr, lo, i - 1)
    inPlayQuickSortHelper(arr, i + 1, hi)

def inPlaceQuickSort(arr):
    inPlayQuickSortHelper(arr,0,len(arr)-1)
    return arr


array = [5,4,3,2,1]
print(inPlaceQuickSort(array))