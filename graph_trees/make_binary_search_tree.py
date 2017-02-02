from tree import Tree

def make_bstree(t,array, first, last):
	'''
	Time Complexity = O(n)
	Space Complexity = O(1)
	'''
	if first <= last:
		mid = (first + last)//2
		n = t.make_node(array[mid])
		n.lchild = make_bstree(t,array,first,mid-1)
		n.rchild = make_bstree(t, array, mid+1, last)
		return n

def main():
	t = Tree()
	array = [1,2,3,4,5,6,7,8,9]
	make_bstree(t,array,0,len(array)-1)
	t.preorder()
	print("\n")

if __name__ == '__main__':
	main()