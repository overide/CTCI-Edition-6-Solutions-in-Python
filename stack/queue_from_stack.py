# Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
class MyQueue:

	def __init__(self, size):

		self.size = size
		self.primary = []
		self.aux = []

	def push(self, item):

		if self.is_full():
			print("Stack Overflow!")
			return
		self.primary.append(item)
		print("Successfully pushed {}".format(item))

	def pop(self):
		if self.is_empty():
			print("Stack Underflow!")
			return
		if not self.aux:
			while(self.primary):
				self.aux.append(self.primary.pop())
		pop_item = self.aux.pop()

		print("Successfully poped {}".format(pop_item))
		return pop_item

	def is_full(self):
		return (len(self.primary)+len(self.aux) >= self.size)

	def is_empty(self):
		return (len(self.primary)+len(self.aux) == 0)

def main():
	q = MyQueue(5)
	q.push(1)
	q.push(2)
	q.push(3)
	q.push(4)
	q.push(5)
	q.pop()
	q.pop()
	q.pop()
	q.push(34)
	q.push(12)
	q.push(75)
	q.push(97)

if __name__ == '__main__':
	main()