# 1.1
def isUnique(s):
    hashMap = [0]*256
    for i in s:
        ival = ord(i)
        if hashMap[ival]:
            return False
        hashMap[ival]=1
    return True


def isUniqueBitVector(s):
    bv = 0
    for i in s:
        ival = ord(i)
        if bv & (1 << ival):
            return False
        bv = bv | (1 << ival)
    return True

print("TESTING")
print(isUnique("abcde"))
print(isUnique("abcdea"))
print(isUniqueBitVector("abcde"))
print(isUniqueBitVector("abcdea"))


def createCountMap(a):
    aCounts = {}
    for c in a:
        if c in aCounts:
            aCounts[c] += 1
        else:
            aCounts[c] = 1
    return aCounts

def isPermutation(a,b):
    if len(a) != len(b):
        return False
    aCounts = createCountMap(a)
    bCounts = createCountMap(b)
    for c in a:
        if aCounts[c] != bCounts[c]:
            return False
    return True


print("Test Permutation")
print(isPermutation("abba","bbaa"))
print(isPermutation("abbc","bbaa"))
print(isPermutation("abbc","bbaad"))


def countChar(char, inputString, end):
    count = 0
    for i in range(0,end):
        c = inputString[i]
        if c == char:
            count += 1
    return count

## MISTAKES: forgot 3 instead of 2 for end count
## bytearray issues
## ord -> chr remember differences and correct types for conversions

def URLify(inputString, end):
    wsCount = countChar(" ", inputString, end)
    inputString = bytearray(inputString, 'utf-8')
    
    finalStringLength = end+2*wsCount #2 extra letters added with `%02` not 2S
    ogStringLength = end

    insertIndex = finalStringLength-1
    readIndex = ogStringLength-1

    while(readIndex >= 0):
        curChar = inputString[readIndex]
        if chr(curChar) ==  " ":
            inputString[insertIndex]    = ord("0")
            inputString[insertIndex-1]  = ord("2")
            inputString[insertIndex-2]  = ord("%")
            insertIndex -= 3
        else:
            inputString[insertIndex] = curChar
            insertIndex -= 1
        readIndex -= 1

    return inputString.decode()

print("Test URLify")
print(URLify("Mr John Smith              ",13))

def permutationPalindrome(inputString):
    ## reduce string to letters
    countMap = {}
    for c in inputString.lower():
        if c.isalpha():
            if c in countMap:
                countMap[c] += 1
            else:
                countMap[c] = 1

    theOddCounter = 0
    for key, _ in countMap.items():
        #if odd
        if countMap[key] % 2 == 1:
            theOddCounter += 1
        if theOddCounter > 1:
            return False
    return True

## CORRECT

print("Testing Permutation Palindrome")
print(permutationPalindrome("abba")) #True
print(permutationPalindrome("abbc")) #False
print(permutationPalindrome("abbbaccc")) #False
print(permutationPalindrome("abbacccddd")) #False
print(permutationPalindrome("aabbcccdd")) #True
print(permutationPalindrome("Tact Coa")) #True


## MISTAKES swapped check helper a/b values
## Needed hint to recognize that checkhelper remove/insert are the SAME just swapped

#default is remove, swap for insert check
def checkHelper(a,b):
    j = 0
    skipCounter = 0
    for i in range(0,len(b)):
        while b[i] != a[j]:
            skipCounter += 1
            j += 1
        j += 1
    return not skipCounter > 1

def checkReplaceHelper(a,b):
        editCounter = 0
        for i in range(0,len(a)):
            if a[i] != b[i]:
                editCounter += 1
        return not editCounter > 1

def checkEdit(a,b):
    #insert
    if len(a) == len(b) + 1:
        return checkHelper(a,b)
    #remove
    elif len(a) == len(b) - 1:
        return checkHelper(b,a)
    #replace
    elif len(a) == len(b):
        return checkReplaceHelper(a,b)
    return False

print("Testing Check Edit")
print(checkEdit("pale","ple"))
print(checkEdit("pales","pale"))
print(checkEdit("pale","bale"))
print(checkEdit("pale","bake"))

def stringCompression(inputString):
    pass