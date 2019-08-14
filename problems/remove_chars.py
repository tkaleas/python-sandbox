## PROBLEM
# Write an efficient funciton that deletes chars from a mutable string.
# INPUT str and remove
# Example "Battle of the Vowels: Hawaii vs. Grozny" `aeiou`
#   Output: "Bttle f the Vwls: HW vs. Grzny"

#SOLUTION
# construct a hashmap of the removeable characters -> bool map, remove or do not remove.
# two pointers, one is parsing the strings, and one is removing the things in the hashmap


def removeSpecifiedChars(inputString, removeString):

    removeCharList = [False]*256    # Assumes ASCII string, for unicode would be 0 to 65535

    #Parse Remove String
    for c in removeString:
        removeCharList[ord(c)] = True
    
    #Parse CharList String

    insertPoint = 0
    for i in range(0,len(inputString)):
        curChar = inputString[i]
        # if its in the char list
        if removeCharList[ord(curChar)]: