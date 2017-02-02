# Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
# this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
# node never differ by more than one.

from tree import Tree

def is_balanced(root,height=0):
	'''
	Time Complexity : O(n)
	Space COmplexity : O(h) //due to recursion
	'''
	if root.lchild == None and root.rchild == None:
		return height

	lsubtree = None
	rsubtree = None
	if root.lchild == None:
		rsubtree = height
		lsubtree = is_balanced(root.lchild, height+1)
	elif root.rchild == None:
		lsubtree = height
		rsubtree = is_balanced(root.rchild, height+1)
	else:
		lsubtree = is_balanced(root.lchild, height+1)
		rsubtree = is_balanced(root.rchild, height+1)

	if not(lsubtree and rsubtree):
		return False

	elif abs(rsubtree - rsubtree)>1:
		return False
	else:
		return max(lsubtree,rsubtree)

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
	n2.lchild = n4
	n2.rchild = n5
	n3.lchild = n6
	n3.rchild = n7
	n5.rchild = n8
	print(t.root.data)
	print(is_balanced(t.root))
if __name__ == '__main__':
	main()