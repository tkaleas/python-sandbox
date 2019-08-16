def getChar(key,place):
    if place < 1 or place > 3:
        raise Exception("Place Out Of Bounds")

    if key < 2 or key > 9:
        raise Exception("Key Out Of Bounds")

    tmap = {2 : ["A","B","C"],
            3 : ["D","E","F"],
            4 : ["G","H","I"],
            5 : ["J","K","L"],
            6 : ["M","N","O"],
            7 : ["P","R","S"],
            8 : ["T","U","V"],
            9 : ["W","X","Y"]
                 }
    return tmap[key][place-1]

def telephone(arr):
    cTotal = []
    
    if (len(arr) < 1):
        return []

    d = arr[0]

    if (len(arr) == 1):
        d = arr[0]
        if d < 2:
            cTotal.append("1")
        else:
            for i in range(1,4):
                c = getChar(d,i)
                cTotal.append(c)
        return cTotal

    #get sub combos
    subCombos = telephone(arr[1:])
    if d < 2:
        cTotal = ["1"+a for a in subCombos]
    else:
        for i in range(1,4):
            c = getChar(d,i)
            cTotal.extend([c+a for a in subCombos])
    return cTotal

print(telephone([1,5,7,3,6,4,3]))