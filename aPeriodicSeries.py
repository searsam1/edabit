def sumString(s): return str(sum(int(i) for i in s)) 

def getNextTerm(string):
    summedString = sumString(string)
    nextTerm = string + summedString
    chop = len(summedString)
    return nextTerm[chop:]

def periodic(s):
    nextTerm = getNextTerm(s) 
    arr = [s, nextTerm]
    while len(arr) == len(set(arr)):
        nextTerm = getNextTerm(nextTerm)
        arr.append(nextTerm)
    return len(arr) - 1
print(periodic("1234567"))