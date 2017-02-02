
from tree import Tree

def make_level_list(root,lst,level=0):
		if root != None:
			if len(lst) == level:
				lst.append([root.data])
			else:
				lst[level].append(root.data)
			make_level_list(root.lchild,lst,level+1)
			make_level_list(root.rchild,lst,level+1)

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
	lst = []
	make_level_list(t.root,lst)
	print(lst)

if __name__ == '__main__':
	main()




