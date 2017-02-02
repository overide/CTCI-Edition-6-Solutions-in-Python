# BST Sequences: A binary search tree was created by traversing through an array from left to right
# and inserting each element. Given a binary search tree with distinct elements, print all possible
# arrays that could have led to this tree.

from tree import Tree

def permute (prefix, lst_l, lst_r):
	if lst_l == None or lst_r == None:
		return lst_l if lst_l is not None else lst_r

	permutations = []
	for l1 in lst_l:
		for l2 in lst_r:
			permutations.append([prefix] + l1 + l2)
			permutations.append([prefix] + l2 + l1)

	return permutations

def bst_sequence(root):
	if root is not None:
		if root.lchild == None and root.rchild == None:
			return [[root.data]]

		l_subtree = bst_sequence(root.lchild)
		r_subtree = bst_sequence(root.rchild)

		permutation = permute(root.data,l_subtree,r_subtree)
		return permutation
	else:
		return None 

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
	[print(l) for l in bst_sequence(t.root)]

if __name__ == "__main__":
	main()
