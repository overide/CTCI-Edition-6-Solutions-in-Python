# implement k stack in single array, simply generalized the question

class kstack:
	'''
	Time Complexity of push : O(1)
	Time Complexity of pop : O(1)
	Space Complexity : O(2n + k)
	where :
	n is size of array we take
	k is number of stack we want

	You might argue about 2n + k extra space, yeah! for small data, it's awful 
	but think about big picture when array hold the reference of big data (say 100 bytes)
	then in comparison to that space, it's negligbile and then it would be better approach. 
	'''

	def __init__(self,no_of_stack,size_array):
		self.k = no_of_stack
		self.n = size_array 
		self.arr = [0 for _ in range(self.n)]
		self.top = [-1 for _ in range(self.k)]# keeps index of top of each of k stacks  
		self.nxt = [i+1 for i in range(self.n)]
		self.nxt[self.n-1] = -1 #-1 to show end of list
		self.free = 0 #store index of next free space in arr

	def push(self,item,sn):
		if self.is_full():
			print("Stack Overflow!")
			return 

		i = self.free
		assert i<self.k,"i : {}, out of range".format(i)

		#Update index of free slot to the next free slot in arr
		self.free = self.nxt[i]

		#update next to the index of top element perviously in stack sn
		# -1 indicate no top 
		self.nxt[i] = self.top[sn]

		# update top to the current index at which it is
		self.top[sn] = i

		#finally store the element in the arr
		self.arr[i] = item
		print("Seccessfully pushed {} in stack {}".format(item,sn))

	def pop(self, sn):

		if self.is_empty(sn):
			print("Stack Underflow!")
			return
	
		i = self.top[sn]
		pop_item = self.arr[i]

		#set top to index of pervious top
		self.top[sn] = self.nxt[i]

		#now nxt[i] shows next availabe slot, Dual purpose!!
		self.nxt[i] = self.free

		#update free to point currently freed slot i
		self.free = i
		print("Successfully popped {} form stack {}".format(pop_item,sn))
	def is_full(self):
		return self.free == -1

	def is_empty(self,sn):
		return self.top[sn] == -1

def main():
	k = 3 #no of stack
	stack = kstack(k,12)
	stack.push(2,0)
	stack.push(3,0)
	stack.push(4,1)
	stack.push(5,1)
	stack.push(7,2)
	stack.push(9,2)
	stack.push(12,0)
	stack.push(59,2)
	stack.push(96,2)

	stack.pop(0)
	stack.pop(0)
	stack.pop(0)
	stack.pop(0)
	stack.pop(2)
	stack.pop(2)

if __name__ == '__main__':
	main()