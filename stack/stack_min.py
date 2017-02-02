# Stack Min: How would you design a stack wh ich, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.

from math import inf
class stack:
	'''
	Here we keep track on minimum element whenever 
	any new item is pushed or popped on the stack
	
	n = size of stack
	set_new_min() method time complexity : O(n)

	'''
	def __init__(self,size):
		self.array = []
		self.min = inf
		self.MAX = size

	def push(self, item):
		if self.is_full():
			print("stack overflow!")
			return 
		if item < self.min:
			self.min = item
		self.array.append(item)
		print("Successfully pushed {}".format(item))

	def pop(self):
		if self.is_empty():
			print("Stack Underflow!")
			return
		pop_item = self.array.pop()
		if pop_item is self.min:
			self.set_new_minimum()
		print("Successfully popped {}".format(pop_item))
		return pop_item

	def minimum(self):
		return self.min

	def set_new_minimum(self):
		self.min = inf
		for item in self.array:
			if item < self.min:
				self.min = item

	def is_full(self):
		return(len(self.array) == self.MAX)

	def is_empty(self):
		return (len(self.array) == 0)

class stackv2:
	'''
	Here we keep track on minimum element by using another stack
	named min_stack

	Additional Space = O(n)
	'''

	def __init__(self,size):
		self.array = []
		self.min_stack = [inf]
		self.MAX = size

	def push(self,item):
		if item < self.min_stack[-1]:
			self.min_stack.append(item)

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
		if pop_item is self.min_stack[-1]:
			self.min_stack.pop()

		print("Successfully popped {}".format(pop_item))
		return pop_item

	def minimum(self):
		return self.min_stack[-1]

	def is_full(self):
		return(len(self.array) == self.MAX)

	def is_empty(self):
		return (len(self.array) == 0)

def main():

	s = stackv2(6)
	s.push(2)
	s.push(3)
	s.push(4)
	s.push(1)
	s.push(-1)
	print("minimim : {}".format(s.minimum()))
	s.pop()
	print("minimim : {} ".format(s.minimum()))
	s.pop()
	print("minimim : {}".format(s.minimum()))
	s.pop()
	print("minimim : {}".format(s.minimum()))

if __name__ == '__main__':
	main()