# Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to
# find the length of the longest sequence of 1 s you could create.
# EXAMPLE
# Input: 1775
# Output: 8
# (or: 11011101111

def longest_sequence(n):
	'''
	Time Complexity : O(b)
	b = bits in number
	Space Complexity : O(1)
	'''
	if ~n == 0:return n.bit_length()

	previous_len = 0
	current_len = 0
	max_length = 1
	mask = 1

	for _ in range(n.bit_length()):
		if n & mask >= 1:
			current_len += 1
		else:
			previous_len = 0 if n & (mask<<1) == 0 else current_len
			current_len = 0

		max_length = max(previous_len + current_len + 1, max_length)
		mask <<= 1

	return max_length

def main():
	n = int(input("Enter an integer: ").strip(' '))
	print("Longest 1's sequence : ",longest_sequence(n))

if __name__ == '__main__':
	main()