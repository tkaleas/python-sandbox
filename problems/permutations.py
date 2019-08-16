def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)

def getPermutations(inputStr):
    # Base Case
    if len(inputStr) < 2:
        return [inputStr]

    total = []
    
    #for c in inputStr:
    for i in range(0,len(inputStr)):
        c = inputStr[i]
        permInput = swap(inputStr,i, 0)
        c = inputStr[i]
        temp = [c+a for a in getPermutations(permInput[1:])]
        total.extend(temp)

    return total

## THIS ONE IS THE WORKING SOLUTION
# algorithm involves temporary "output" string
out = ""
totalCombos = []
def getCombo(istr, start):
    global out
    global totalCombos
    for i in range(start,len(istr)):
        out += istr[i]
        totalCombos.append(out)
        if i < len(istr):
            getCombo(istr,i+1)
        out = out[:-1]
    return totalCombos

## DOESNT WORK: OUTPUTS TOO MANY COMBINATIONS
def getCombinations(inputStr):

    if len(inputStr) < 2:
        return [inputStr]

    total = []

    for i in range(0,len(inputStr)):
        c = inputStr[i]
        combo = getCombinations(inputStr[i+1:])
        total += [ c + a for a in combo ]
        total.extend(combo)

    return total
    