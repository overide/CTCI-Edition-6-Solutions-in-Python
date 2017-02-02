# Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.

class stack:
	'''
	Additional Space = O(n)
	sort() method time complexity : O(n^2)
	'''

	def __init__(self,size):
		self.array = []
		self.aux = []
		self.MAX = size

	def push(self,item):

		if self.is_full():
			print("stack overflow!")
			return 
		self.array.append(item)
		print("Successfully pushed {}".format(item))

	def pop(self):
		if self.is_empty():
			print("Stack Underflow!")
			return

		pop_item = self.array.pop()
		print("Successfully popped {}".format(pop_item))
		return pop_item

	def peek(self):
		return self.array[-1]

	def sort(self):
		self.aux.append(self.array.pop())
		pop_counter = 0
		while(self.array):
			cur_item = self.array.pop()
			while self.aux and self.aux[-1]<cur_item:
				pop_counter += 1
				self.array.append(self.aux.pop())
			self.aux.append(cur_item)
			while(pop_counter):
				pop_counter -= 1
				self.aux.append(self.array.pop())

		self.array,self.aux = self.aux,self.array

	def is_full(self):
		return(len(self.array) == self.MAX)

	def is_empty(self):
		return (len(self.array) == 0)

def main():

	s = stack(6)
	s.push(2)
	s.push(3)
	s.push(4)
	s.push(1)
	s.push(-1)
	s.sort()
	s.pop()
	s.pop()
	s.pop()
	s.pop()
	s.pop()
if __name__ == '__main__':
	main()