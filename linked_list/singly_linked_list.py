# very quick implementation of the singly linked list

class Node :
	_data = None
	_next = None

	def __init__(self ,d=None):
		self._data = d

	def set_data(self, d):
		self._data = d

	def set_next(self, l):
		self._next = l

	def get_next(self):
		return self._next

	def get_data(self):
		return self._data

	def __str__(self):
		return str(self._data)

class Linked_list :
	_head = None
	_length = 0

	def get_head(self):
		return self._head
	
	def set_head(self,h):
		self._head = h

	def append(self, d):
		n = Node(d)

		if self._head == None :
			self._head, self._length = n, self._length+1
		else:
			tmp_head = self._head
			while(tmp_head.get_next() != None):
				tmp_head = tmp_head.get_next()
			tmp_head.set_next(n)
			self._length += 1

	def __len__(self):
		return self._length

	def __iter__(self):
		tmp_head = self._head
		while(tmp_head != None):
			yield tmp_head.get_data()
			tmp_head = tmp_head.get_next()