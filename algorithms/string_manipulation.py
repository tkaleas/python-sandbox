def reverser(s):
    #splicing syntax
    return s[::-1]
    
def reverser2(s):
    #standard method
    out = ""
    for c in range(len(s),0,-1):
        out = out + s[c-1]
    return out