# Pairwise Swap: Write a program to swap odd and even bits in an integer with as few instructions as
# possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on)

def swap(n):
	'''
	Time Complexity : O(1)
	Space Complexity : O(1)
	0xaaaaaaaa is hexadecimal equivalent to 10101010101010101010101010101010
	0x55555555 is hexadecimal equivalent to 01010101010101010101010101010101
	'''
	return ((n & 0xaaaaaaaa)>>1)|((n & 0x55555555)<<1)

def main():
	n = int(input())
	print(swap(n))

if __name__ == '__main__':
	main()