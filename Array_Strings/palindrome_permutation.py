# Palindrome Permutation: Given a string, write a function to check if it is a permutation of
# a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
# permutation is a rearrangement of letters. The palindrome does not need to be limited to just
# dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations:"taco cat'; "atco cta '; etc.)

from collections import Counter

def isPermutationOfPalindrome(string):
	no_odd_count = 0
	char_counter = Counter(string)
	if char_counter.get(' '):
		del char_counter[' ']

	for ch, count in char_counter.items():
		if no_odd_count <= 1:
			if not isEven(count):
				no_odd_count += 1
		else:
			return False

	return False if no_odd_count>1 else True

def isEven(count):
	if count % 2 == 0:
		return True
	else:
		return False

def main():
	print(isPermutationOfPalindrome(input()))

main()