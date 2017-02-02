# Check Subtree: Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
# algorith m to determine if T2 is a subtree of Tl .

from tree import Tree

def is_subtree(t1, t2):
	'''
	Time Complexity : O(n + m)
	Space Complexity : O(n + m)
	'''
	pret1 = [];pret2 = [];int1 = [];int2 = []
	inorder(t1,int1);preorder(t1,pret1);inorder(t2,int2);preorder(t2,pret2)
	pret1 = "".join(pret1);int1 = "".join(int1);pret2 = "".join(pret2);int2 = "".join(int2)

	if int1.find(int2) != -1 and pret1.find(pret2) != -1:
		return True 
	else:
		return False

def inorder(root, lst):
	if root is not None:
		inorder(root.lchild, lst)
		lst.append(str(root.data))
		inorder(root.rchild, lst)

def preorder(root, lst):
	if root is not None:
		lst.append(str(root.data))
		preorder(root.rchild, lst)
		preorder(root.lchild, lst)

def main():

	t1 = Tree()
	n1 = t1.make_node(1)
	n2 = t1.make_node(2)
	n3 = t1.make_node(3)
	n4 = t1.make_node(4)
	n5 = t1.make_node(5)
	n6 = t1.make_node(6)
	n7 = t1.make_node(7)

	n1.lchild = n2
	n1.rchild = n3
	n2.lchild = n4
	n2.rchild = n5
	n3.lchild = n6
	n3.rchild = n7

	t2 = Tree()
	n8 = t2.make_node(3)
	n9 = t2.make_node(6)
	n10 = t2.make_node(7)

	n8.lchild = n9
	n8.rchild = n10

	print(is_subtree(t1.root,t2.root))
if __name__ == "__main__":
	main()