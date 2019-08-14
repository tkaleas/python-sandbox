# PROBLEM Write an efficient function to find the first nonrepeated character 
# in a string. For instance, the first nonrepeated character in “total” is ‘o’ 
# and the first nonrepeated character in “teeter” is ‘r’. Discuss the efficiency of your algorithm.

#INPUT string
#OUTPUT char

# SOLUTION
# - create bool list size of 256, one for each characterpython, fill with 0
# - 1st pass for each character add to character count
# - 2nd pass for each character check count in array, if its 1 then return. O(n), O(1) since only requires an array of 256 values

def nonrepeatedChar( inputString ):
    charCountList = [0]*256    # Assumes ASCII string, for unicode would be 0 to 65535
    # Parse Count
    for char in inputString:
        charCountList[ord(char)] += 1
    for char in inputString:
        if charCountList[ord(char)] == 1:
            return char
    return None 
