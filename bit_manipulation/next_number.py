# Next Number: Given a positive integer, print the next smallest and the next largest number that
# have the same number of 1 bits in their binary representation

def find_largest(n):
	'''
	Time Complexity : O(b)
	Space Complexity : O(1)
	'''
	if n == 0:
		return 1

	elif (n+1 & n) == 0: #all 1's bits
		bit_len = n.bit_length()
		mask = (1 << (bit_len - 1))-1
		n = 1<<bit_len
		n |= mask
		return n
	else:
		mask = 1
		ones_count = 0
		bit_count = 0
		for _ in range(n.bit_length()):
			bit_count += 1
			if n & mask >= 1:
				ones_count += 1
				if n & mask<<1 == 0:
					break
			mask <<= 1

		mask <<= 1
		n = (n & ~(mask-1))| mask
		n |= (1<<(ones_count-1)) - 1
		return n

def find_smallest(n):

	'''
	Time Complexity : O(b)
	Space Complexity : O(1)
	'''

	if n == 0:
		print(" No positive minimum possible ")
		return
	elif (n+1 & n) == 0: # all 1's bit 
		print("No positive min with same 1's possible ")
		return
	else:
		bit_count = -1
		mask = 1
		for _ in range(n.bit_length()):
			bit_count += 1
			if not n & mask:
				if n & mask<<1:
					break
			mask <<= 1
		mask1 = (1<<bit_count)-1
		mask2 = -1<<bit_count+2

		left_bits = n & mask1
		n &= mask2 #clearing 
		n |= left_bits
		n |= (1<<bit_count)
		return n

def main():
	n = int(input().strip(' '))
	print("Next largest: ", find_largest(n))
	print("Next Smallest: ", find_smallest(n))

if __name__ == '__main__':
	main()