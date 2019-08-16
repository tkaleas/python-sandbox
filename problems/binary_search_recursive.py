# Gotchas In Interview:
# Handle Exceptions and issues with input:
## List these out properly:
## FORGOT to add lo to mid calculation: mid = (hi-lo)/2 + lo

def binarySearchRec(sortedArray, val, hi, lo):

    if sortedArray.empty():
        return False

    mid = int((hi-lo)/2) + lo

    if sortedArray[mid] == val:
        return mid
    elif sortedArray[mid] < val:
        #search bottom half
        return binarySearchRec(sortedArray, val, mid-1, lo)
    elif sortedArray[mid] > val:
        #search top half
        return binarySearchRec(sortedArray, val, hi, mid + 1)

    return False