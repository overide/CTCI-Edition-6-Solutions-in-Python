# problem statement : Is Unique: Implement an algorithm to determine if a string has 
# all unique characters. What if you cannot use additional data structures?

def isUnique(string):
	string = list(string)
	countmap = {}
	for ch in string:
		if countmap.get(ch):
			return False
		else:
			countmap[ch]=1

	return True

def main():
	print(isUnique(input()))

main()