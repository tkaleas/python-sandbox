import datastructures.linkedlist

from datastructures.linkedlist import LinkedList, LinkedListElement

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
    curChar = inputString[0]
    curCount = 1
    curIndex = 1
    outputString = ""
    
    while curIndex < len(inputString):
        if inputString[curIndex] == curChar:
            curCount += 1
        else:
            outputString += curChar + str(curCount)
            curCount = 1
            curChar = inputString[curIndex]
        curIndex += 1

    outputString += curChar + str(curCount)

    if len(outputString) < len(inputString):
        return outputString
    
    return inputString

print("Testing stringCompression")
print(stringCompression("aabcccccaaa"))
print(stringCompression("a"))
print(stringCompression("abcde"))

def rotateShell(arr,rowStart, rowEnd):

    for i in range(rowStart, rowEnd):

        #TRICK HERE: difference between row start and row end
        diff = i - rowStart

        #Do 4 Rotations
        t = arr[rowStart][i]
        r = arr[i][rowEnd]
        b = arr[rowEnd][rowEnd-diff]
        l = arr[rowEnd-diff][rowStart]

        # place in array
        arr[i][rowEnd] = t
        arr[rowEnd][rowEnd-diff] = r
        arr[rowEnd-diff][rowStart] = b
        arr[rowStart][i] = l

    return arr

# coordinates are flipped, (y,x) (row, column)
def rotateArray(arr):

    n = len(arr)

    for i in range(0, int(n/2), 1):
        rowStart = i
        rowEnd = n-i-1
        rotateShell(arr,rowStart,rowEnd)
        print("rowStart {} rowEnd {}".format(rowStart,rowEnd))
        print(*arr, sep = "\n")
        print("\n")
    return arr

arr0 = [ [1,2],
         [3,4] ]

arr = [ [1,2,3],
        [4,5,6],
        [7,8,9]]

arr2 = [ [ 1,  2,  3,  4],
         [ 5,  6,  7,  8],
         [ 9, 10, 11, 12],
         [13, 14, 15, 16] ]

print("Testing Rotate Array")
print(*rotateArray(arr0), sep = "\n")
print("\n")
print(*rotateArray(arr), sep = "\n")
print("\n")
print(*rotateArray(arr2), sep = "\n")


def setColZero(col, mat):
    for i in range(0,len(mat)):
        mat[i][col] = 0

def setRowZero(row, mat):
    row = mat[row]
    for i in range(0,len(row)):
        row[i] = 0

def zeroMatrix(mat):

    rowList = []
    columnList = []

    #LOOP ROW = Y
    for y in range(0,len(mat)):
        # LOOP COL = X
        for x in range(0,len(mat[y])):
            if mat[y][x] == 0:
                rowList.append(y)
                columnList.append(x)

    # Set Zeros
    for row in rowList:
        setRowZero(row,mat)
    for col in columnList:
        setColZero(col,mat)
    return mat

arr0 = [ [1,2],
         [0,4] ]

arr = [ [1,2,3],
        [4,0,6],
        [7,8,9]]

arr2 = [ [ 1,  2,  3,  0],
         [ 5,  6,  7,  8],
         [ 0, 10, 11, 12],
         [13, 14, 15, 16] ]

print("Testing Zero Matrix")
print(*zeroMatrix(arr0), sep = "\n")
print(*zeroMatrix(arr), sep = "\n")
print(*zeroMatrix(arr2), sep = "\n")

# 2.1 Remove Dups

def removeLinkedListElem(prev, elem, nex):
    del elem
    prev.next = nex

def removeDups(ll):
    # count the number
    theMap = {}
    cur = ll.head
    prev = None

    while cur is not None:
        nex = cur.next
        if cur.value in theMap:
            removeLinkedListElem(prev,cur,nex)
        else:
            theMap[cur.value] = True
        prev = cur
        cur = cur.next

def getLength(node):
    if node is None:
        return 0
    return 1 + getLength(node.next)

def kToLast(ll, k):
    listLength = getLength(ll.head)
    position = listLength - k - 1

    cur = ll.head
    i = 0

    while(i < position and cur is not None):
        i += 1
        cur = cur.next

    return cur.value

e1 = LinkedListElement(1)
e2 = LinkedListElement(2)
e3 = LinkedListElement(3)
e4 = LinkedListElement(4)
e5 = LinkedListElement(5)
e6 = LinkedListElement(6)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)
ll.append(e6)

print("Test K To Last")
print(getLength(e1))
print(kToLast(ll,0))
print(kToLast(ll,1))
print(kToLast(ll,2))
print(kToLast(ll,3))
print(kToLast(ll,4))
print(kToLast(ll,5))


def delNode(node):
    cur = node
    prev = None
    while cur.next is not None:
        cur.value = cur.next.value
        prev = cur
        cur = cur.next
    if prev.next is not None:
        prev.next = None

print("Test Del Middle Node")
delNode(e3)
print(ll.toList())
delNode(e2)
print(ll.toList())
delNode(e2)
print(ll.toList())


def partitionLinkedList(ll, x):
    cur = ll.head

    lEnd = rEnd = lStart = rStart = None

    while cur:
        if cur.value < x:
            #left list
            if lStart:
                lEnd.next = cur
                lEnd = lEnd.next
            else:
                lStart = cur
                lEnd = cur
        else:
            #right list
            if rStart:
                rEnd.next = cur
                rEnd = rEnd.next
            else:
                rStart = cur
                rEnd = cur

        cur = cur.next

    #reattach linked lists back to eachother
    if lEnd:
        lEnd.next = rStart
    if rEnd:
        rEnd.next = None

    ll.head = lStart
    return ll

e1 = LinkedListElement(3)
e2 = LinkedListElement(5)
e3 = LinkedListElement(8)
e4 = LinkedListElement(5)
e5 = LinkedListElement(10)
e6 = LinkedListElement(2)
e7 = LinkedListElement(1)


ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)
ll.append(e6)
ll.append(e7)


print("Test Partition")
partitionLinkedList(ll,5)
print(ll.toList())

def sumListsHelper(firstNode, secondNode, carry):

    a = firstNode.value if firstNode else 0
    b = secondNode.value if secondNode else 0

    val = (a + b + carry) % 10
    carry = int((a + b + carry) / 10)

    newNode = LinkedListElement(val)

    firstNext = firstNode.next if firstNode else None
    secondNext = secondNode.next if secondNode else None

    if firstNext and secondNext:
        newNode.next = sumListsHelper(firstNext, secondNext, carry)
    else:
        newNode.next = None

    return newNode

def sumLists(firstList, secondList):
    return LinkedList(sumListsHelper(firstList.head, secondList.head, 0))

print("Test Sum Lists")

e1 = LinkedListElement(7)
e2 = LinkedListElement(1)
e3 = LinkedListElement(6)

e4 = LinkedListElement(5)
e5 = LinkedListElement(9)
e6 = LinkedListElement(2)

l1 = LinkedList(e1)
l1.append(e2)
l1.append(e3)


l2 = LinkedList(e4)
l2.append(e5)
l2.append(e6)

suml = sumLists(l1,l2)
print(suml.toList())

def isPalindromeRecurse(curNode, depth, listLen):

    odd = True if listLen % 2 == 1 else False

    # Base Case for Middle
    if odd and depth > int(listLen/2):
        return (True, curNode.next)
    elif not odd and depth >= int(listLen/2)+1:
        return (True, curNode)

    isPal, endNode = isPalindromeRecurse(curNode.next, depth + 1, listLen)

    #negative result kick back up
    if not endNode or not isPal:
        return (False, None)

    return (isPal and curNode.value == endNode.value, endNode.next)

def linkedListIsPalindrome(ll):
    n = getLength(ll.head)
    isPal, _ = isPalindromeRecurse(ll.head, 1, n)
    return isPal

print("Test LinkedList IsPalindrome")

e1 = LinkedListElement("a")
e2 = LinkedListElement("b")
e3 = LinkedListElement("c")
e4 = LinkedListElement("d")
e5 = LinkedListElement("c")
e6 = LinkedListElement("b")
e7 = LinkedListElement("a")
l1 = LinkedList(e1)
l1.append(e2)
l1.append(e3)
l1.append(e4)
l1.append(e5)
l1.append(e6)
l1.append(e7)
print(linkedListIsPalindrome(l1))

e1 = LinkedListElement("a")
e2 = LinkedListElement("b")
e3 = LinkedListElement("c")
e5 = LinkedListElement("c")
e6 = LinkedListElement("b")
e7 = LinkedListElement("a")
l1 = LinkedList(e1)
l1.append(e2)
l1.append(e3)
l1.append(e5)
l1.append(e6)
l1.append(e7)
print(linkedListIsPalindrome(l1))

# get linked list as a stack of linked list nodes
def getListStack(l):
    cur = l.head
    stack = []
    while cur:
        stack.append(cur)
        cur = cur.next
    return stack

# get linked list as a stack of linked list nodes
def listIntersect(A,B):
    
    stackA = getListStack(A)
    stackB = getListStack(B)
    print([x.value for x in stackA])
    print([x.value for x in stackB])

    if len(stackA) < 1 or len(stackB) < 1:
        #maybe better to throw an error here
        return None

    prevVal = None
    curNodeA = stackA.pop()
    curNodeB = stackB.pop()

    # check for reference versus value
    while (curNodeA is curNodeB) and len(stackA) > 0 and len(stackB) > 0:
        prevVal = curNodeA.value
        curNodeA = stackA.pop()
        curNodeB = stackB.pop()

    return prevVal

e1 = LinkedListElement("a")
e2 = LinkedListElement("b")
e3 = LinkedListElement("c")
e4 = LinkedListElement("d")
e5 = LinkedListElement("e")
e6 = LinkedListElement("f")
e7 = LinkedListElement("g")
e8 = LinkedListElement("h")
e9 = LinkedListElement("i")

l1 = LinkedList(e8)
l1.append(e6)
l1.append(e5)
l1.append(e4)
l1.append(e3)
l1.append(e2)
l1.append(e1)

l2 = LinkedList(e9)
l2.head.next = e5
#e7.next = e5

print("Testing List Intersect")
print(listIntersect(l1,l2))


class StairCaseSolution(object):

    staircaseMemo = {}

    def staircaseRunner(self, n):
        if n == 1 or n == 0:
            self.staircaseMemo[n] = 1
            #return staircaseMemo[n]
        elif n == 2:
            if n in self.staircaseMemo:
                return self.staircaseMemo[n]
            else:
                self.staircaseMemo[n] = self.staircaseRunner(n-1) + self.staircaseRunner(n-2)
        elif n >= 3:
            if n in self.staircaseMemo:
                return self.staircaseMemo[n]
            else:
               self.staircaseMemo[n] = self.staircaseRunner(n-3) + self.staircaseRunner(n-1) + self.staircaseRunner(n-2)
        return self.staircaseMemo[n]

print("Testing Staircase Runner")
sol = StairCaseSolution()
print(sol.staircaseRunner(155))

def multiply(a,b):
    if b == 1:
        return a
    if b == 0:
        return b
    return (a << 1) + multiply(a, b-2)

print("5*5 == {}".format(multiply(5,5)))
print("1*5 == {}".format(multiply(1,5)))
print("25*5 == {}".format(multiply(25,5)))