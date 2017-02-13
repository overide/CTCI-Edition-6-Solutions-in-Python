import math
def tobin(num):
	if num<0 or num>1:
		print("ERROR")
	else:
		binary_str = "."
		error = False 
		while(1):
			if len(binary_str) >= 33:
				error = True
				break

			product = num * 2
			if product >= 1:
				binary_str = binary_str + str(1)
			else:
				binary_str = binary_str + str(0)

			if product == 1:
				break	
			num = product - math.floor(product)

		if error:
			print("ERROR")
		else:
			print("Binary Equivalent: " + binary_str)

def main():
	num = input("Enter any real number like 0.75: ")
	tobin(float(num))

if __name__ == '__main__':
	main()