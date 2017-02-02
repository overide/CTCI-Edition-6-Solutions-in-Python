class Node:
	def __init__(self,d):
		self.data = d
		self.parent = None
		self.lchild = None
		self.rchild = None

class Tree:
	def __init__(self):
		self.root = None

	def make_node(self,d):
		n = Node(d)
		if self.root == None:
			self.root = n
		return n

	def _preorder(self,root):
		if root != None:
			print(root.data,end=" ")
			self._preorder(root.lchild)
			self._preorder(root.rchild)

	def preorder(self):
		r = self.root
		self._preorder(r)

