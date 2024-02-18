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

# More efficient and readable solution
def periodic(n):
	s, l, terms, count = str(n), len(str(n)), {n}, 1
	while True:
		s = (s + str(sum(map(int, s))))[-l:]
		if s in terms:
			return count
		count += 1
		terms.add(s)
            
import random
n = random.randint(0, 668)
print(n)