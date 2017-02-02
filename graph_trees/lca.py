# First Common Ancestor: Design an algorithm and write code to find the first common ancestor
# of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
# necessarily a binary search tree.

from tree import Tree

def find_lca(root,n1,n2):
	'''
	Time Complexity : O(n)
	Space complexity : O(1)
	'''
	if root == None:
		return None

	if root.data == n1.data or root.data == n2.data:
		return root.data

	l_lca = find_lca(root.lchild, n1, n2)
	r_lca = find_lca(root.rchild, n1, n2)

	if l_lca and r_lca:
		return root.data
	else:
		return l_lca if l_lca is not None else r_lca

def main():

	t = Tree()
	n1 = t.make_node(1)
	n2 = t.make_node(2)
	n3 = t.make_node(3)
	n4 = t.make_node(4)
	n5 = t.make_node(5)
	n6 = t.make_node(6)
	n7 = t.make_node(7)

	n1.lchild = n2
	n1.rchild = n3
	n2.lchild = n4
	n2.rchild = n5
	n3.lchild = n6
	n3.rchild = n7

	print("LCA of {} and {} : {}".format(n4.data, n6.data, find_lca(t.root,n4,n6)))
if __name__ == "__main__":
	main()
