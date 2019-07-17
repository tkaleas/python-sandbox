# Bubble Sort Functions
def bubble_sort(input_list):
    pass

#  MergeSort Functions
def merge_sort(input_list):
    pass


# QuickSort Functions
def partition(array, low, high):
    #pivot = high            # use last element as the pivot
    pivot_val = array[high]
    index_small = low-1
    for index_large in range(low,high):
        if array[index_large] <= pivot_val:
            index_small+=1
            array[index_small], array[index_large] = array[index_large], array[index_small] #python value swap
    #put pivot value in correct place
    array[index_small+1],array[high] =  array[high], array[index_small+1]
    return index_small+1

def quicksort_helper(array, low, high):
    #termination value
    if high > low:
        pivot = partition(array,low,high)
        #sort lower array
        quicksort_helper(array,low,pivot-1)
        #sort higher array
        quicksort_helper(array,pivot+1,high)
    return array

def quicksort(array):
    return quicksort_helper(array,0,len(array)-1)