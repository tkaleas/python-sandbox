def binary_search(input_array, value):
    index_start = 0
    index_end = len(input_array)-1
    # Repeat Until Found or Not In Array (-1)
    while (index_start <= index_end):
        index = (index_end+index_start)/2
        listVal = input_array[index]
        if(listVal == value):
            return index
        elif(listVal < value):
            index_start = index+1
        else:
            index_end = index-1
    return -1

def get_fib(position):
    if position == 0:
        return 0
    if position == 1:
        return 1
    return get_fib(position-1)+get_fib(position-2)