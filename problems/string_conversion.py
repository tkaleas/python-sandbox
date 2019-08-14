def stringToInteger(inputString):

    intStartOffset = ord("0")

    is_neg = False
    
    if inputString[0] == "-":
        is_neg = True

    num_digits = len(inputString)-1 if is_neg  else len(inputString)
    multer = 10**(num_digits-1)
    digit_str = inputString[1:] if is_neg else inputString
    output = 0

    for i in range(0, len(digit_str)):
        intVal = ord(digit_str[i]) - intStartOffset
        output+= multer/(10**i) * intVal

    return int(-1*output if is_neg else output)

def singleDigitToString(inputDigit):
    return chr(inputDigit+ord("0"))

def intToString(val):

    is_neg = val < 0
    
    outString = ""
    cval = abs(val)
    while( cval > 0):
        digit = cval % 10
        outString = singleDigitToString(digit) + outString
        cval = int((cval-digit)/10)
    
    if is_neg:
        outString = "-" + outString
    
    return outString