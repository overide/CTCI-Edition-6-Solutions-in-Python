# Conversion: Write a function to determine the number of bits you would need to flip to convert
# integer A to integer B.
# EXAMPLE
# Input: 29 (or: 11101), 15 (or: 01111)
# Output: 2

def bit_swap_required(n, m):
	'''
	Time Complexity : O(b)
	Space Complexity : O(1)
	'''
	n = n ^ m
	count = 0;
	while(n != 0):
		if n & 1:
			count += 1
		n>>=1
	return count

def main():
	n,m = list(map(int,input("Enter N and M:").strip(' ').split(' ')))
	print(bit_swap_required(n,m))

if __name__ == '__main__':
	main()