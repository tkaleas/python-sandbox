# Solution Bugs:
#   - forgot to check base case ending.

def reverseWords(inputString):

    outputString = bytearray(inputString,'utf-8')

    # Reverse String In Place
    j = len(outputString)-1
    i = 0
    while j > i :
        outputString[i],outputString[j] = outputString[j],outputString[i]
        j -= 1
        i += 1

    #Execute Word Reversal Algorithm
    ip = 0      #insert pointer
    tp = 0      #token pointer
    while ip < len(outputString):
        if tp >= len(outputString) or chr(outputString[tp]) == " ": # either delimiter or hit end of the string
            temp_pointer = tp
            tp -= 1 # back up to correct token
            # reverse word back until last tp == ip
            while tp > ip:
                #start swapping
                outputString[tp], outputString[ip] = outputString[ip], outputString[tp]
                ip += 1
                tp -= 1

            #skip delimiter, move to next
            ip = temp_pointer + 1
            tp = temp_pointer + 1

        else:
            tp += 1

    return str(outputString)
