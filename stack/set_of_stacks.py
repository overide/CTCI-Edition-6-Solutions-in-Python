# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push () and SetOfStacks. pop() should behave identically to a single stack
# (that is, pop ( ) should return the same values as it would if there were just a single stack).

# FOLLOW UP
# Implement a function popAt (intstack.index) which performs a pop operation on a specific sub-stack

class Stacks:
	def __init__(self,threshold):
		self.threshold = threshold
		self.sub_stacks = []

	def push(self,item):
		if not self.sub_stacks:
			s = [item]
			self.sub_stacks.append(s)
		else:
			if self.is_full():
				s = []
				self.sub_stacks.append(s)
			self.sub_stacks[-1].append(item)
		print("Successfully pushed {}".format(item))

	def pop(self,i=-1):
		pop_item = self.sub_stacks[i].pop()

		if not self.sub_stacks[i]:
			self.sub_stacks.pop()
		print("Successfully poped {}".format(pop_item))
		return pop_item

	def pop_at(self,index):
		self.pop(index)	
		
	def is_full(self):
		return len(self.sub_stacks[-1]) == self.threshold

def main():
	s = Stacks(5)
	s.push(1)
	s.push(2)
	s.push(3)
	s.push(4)
	s.push(5)
	s.push(6)
	s.push(7)
	s.push(8)
	s.push(9)
	s.push(10)
	print(s.sub_stacks)
	s.pop()
	s.pop()
	s.pop()
	s.pop()
	print(s.sub_stacks)
	s.pop(0)
	print(s.sub_stacks)
	s.pop()

if __name__ == '__main__':
	main()