def is_narcissistic(n):
	mult = len(str(n))
	
	total = 0 
	for char in str(n):
		total += int(char) ** mult
	return total == n