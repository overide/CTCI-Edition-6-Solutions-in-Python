def insertion(n, m ,i, j):
	i = int(i)
	j = int(j)
	n = int(n,2)
	m = int(m,2)

	mask1 = -1 << (j + 1)
	mask2 = (1 << i) - 1

	least_i_bits = n & mask2 #Capturing least i bits

	n &= mask1 #clearing bits
	n |= least_i_bits

	m = m<<i #Shiftng m to align with n
	n |= m #merging
	return n

def main():
	n, m , i, j = input("Enter N, M, i, j: ").strip().split(" ")
	print(bin(insertion(n,m,i,j)))

if __name__ == '__main__':
	main() 