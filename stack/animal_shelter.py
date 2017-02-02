# Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
# out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type). They cannot select which specific animal they would like. Create the data structures to
# maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat. You may use the built-in Linked List data structure.

class AnimalShelter:

	_arrival_time = -1

	def __init__(self):
		self.animals = []

	def enque(self,typ):
		self._arrival_time += 1
		self.animals.append((typ,self._arrival_time))
		print(typ+" is added succesfully!")

	def deque_any(self):
		print(self.animals[0],'is dequed successfully!')
		return self.animals.pop(0)

	def deque_cats(self):
		for i,animal in enumerate(self.animals):
			if animal[0] == 'C':
				print(animal,'is dequed successfully!')
				return(self.animals.pop(i))

	def deque_dogs(self):
		for i,animal in enumerate(self.animals):
			if animal[0] == 'D':
				print(animal,'is dequed successfully!')
				return(self.animals.pop(i))

def main():
	a = AnimalShelter()
	a.enque('D')
	a.enque('D')
	a.enque('C')
	a.enque('D')
	a.enque('C')
	a.enque('C')
	a.enque('D')
	a.enque('C')
	a.enque('D')
	a.deque_any()
	a.deque_any()
	a.deque_cats()
	a.deque_cats()
	a.deque_dogs()
	a.deque_dogs()

if __name__ == '__main__':
	main()