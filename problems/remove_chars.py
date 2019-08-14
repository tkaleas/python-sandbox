## PROBLEM
# Write an efficient funciton that deletes chars from a mutable string.
# INPUT str and remove
# Example "Battle of the Vowels: Hawaii vs. Grozny" `aeiou`
#   Output: "Bttle f the Vwls: HW vs. Grzny"

#SOLUTION
# construct a hashmap of the removeable characters -> bool map, remove or do not remove.
# two pointers, one is parsing the strings, and one is removing the things in the hashmap

#Runtime: O(n+m)

def removeSpecifiedChars(inputString, removeString):
 
    removeCharList = [False]*256    # Assumes ASCII string, for unicode would be 0 to 65535
    outputString = bytearray(inputString,'utf-8')

    #Parse Remove String
    for c in removeString:
        removeCharList[ord(c)] = True
    
    #Parse CharList String

    insertPoint = 0
    for i in range(0,len(inputString)):
        curChar = inputString[i]
        # if its not in the char list, add string
        if not removeCharList[ord(curChar)]:
            outputString[insertPoint] = outputString[i]
            insertPoint += 1
    
    #ideally, null terminate this at the end at position insertPoint
    #python: not sure how to do this, except for return the string up to that point
    outputString = str(outputString[:insertPoint].decode("utf-8"))
    
    print(outputString)