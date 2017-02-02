# Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
# binary search tree. You may assume that each node has a link to its parent.

from tree import Tree

def find_min(node):
	current_min = node
	if node.lchild:
		current_min = find_min(node.lchild)
	return current_min

def successor(node):
	# How to find successor:
	# 1. If the node has a right child, then the successor is the smallest key in the right subtree.
	# 2. If the node has no right child and is the left child of its parent, then the parent is the successor.
	# 3. If the node is the right child of its parent, and itself has no right child, then the successor
	# to this node is the successor of its parent, excluding this node.

	'''
	Time Complexity : O(log n)
	Space Complexity : O(log n) // Recursion
	'''
	if node.rchild: #if node have right child
		return find_min(node.rchild).data

	if node.parent != None: 
		if node.parent.lchild == node:
			return node.parent.data

		else:
			node.parent.rchild = None
			succ = successor(node.parent)
			node.parent.rchild = node
			return succ
	else:
		return None

def main():
	t = Tree()
	n1 = t.make_node(14)
	n2 = t.make_node(11)
	n3 = t.make_node(16)
	n4 = t.make_node(10)
	n5 = t.make_node(12)
	n6 = t.make_node(15)
	n7 = t.make_node(17)
	n8 = t.make_node(13)
	n1.lchild = n2
	n1.rchild = n3
	n2.parent = n1
	n3.parent = n1

	n2.lchild = n4
	n2.rchild = n5
	n4.parent = n2
	n5.parent = n2

	n3.lchild = n6
	n3.rchild = n7
	n6.parent = n3
	n7.parent = n3

	n5.rchild = n8
	n8.parent = n5
	print("Successor of node {} is: {}".format(n7.data,successor(n7)))

if __name__ == '__main__':
	main()