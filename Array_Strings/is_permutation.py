from collections import Counter

# Problem statement : Check Permutation: Given two strings, 
# write a method to decide if one is a permutation of the other.

'''
def isPermutation(string1, string2):
	# complexity : O(n + nlogn)
	# space : O(1)

	if(len(string1) != len(string2)):
		return False

	string1 = sorted(string1)
	string2 = sorted(string2)

	if(string1 == string2):
		return True
	
	return False
'''

def isPermutation(string1,string2):
	# complexity : O(n)
	# space		: O(n)
	if(len(string1) != len(string2)):
		return False

	string1_count = Counter(string1)
	string2_count = Counter(string2)
	for ch,count in string1_count.items():
		if string2_count.get(ch):
			if string2_count[ch] == count:
				return True
			else:
				break
	return False

def main():
	string1,string2 = input().strip(' ').split(' ')
	print(isPermutation(string1,string2))

main()

