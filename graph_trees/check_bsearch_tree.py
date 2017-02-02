from tree import Tree

last_seen = None

def is_bstree(root):
	'''
	Time Complexity : O(n)
	Space Complexity : O(h) 
	'''

	global last_seen

	if root != None:

		if last_seen == False:
			return 
		else:
			if root.lchild:
				is_bstree(root.lchild)

		if last_seen == None or (last_seen != False and last_seen < root.data):
			last_seen = root.data
		else:
			last_seen = False
			return 

		if last_seen == False:
			return
		else:
			if root.rchild:
				is_bstree(root.rchild)

# def _is_bstree(root,root_key,lchild):
# 	if root.lchild == None and root.rchild == None:
# 		return root.data

# 	lsubtree = rsubtree = None
# 	lvalid = None
# 	rvalid = None

# 	if root.lchild:
# 		lsubtree = _is_bstree(root.lchild,root_key,lchild)
# 	if root.rchild:
# 		rsubtree = _is_bstree(root.rchild,root_key,lchild)

# 	if lchild:
# 		if lsubtree != None:
# 			if lsubtree:
# 				if(lsubtree < root.data and lsubtree < root_key):
# 					lvalid = True
# 				else:
# 					lvalid = False
# 			else:
# 				lvalid = False

# 		if rsubtree != None:
# 			if rsubtree:
# 				if(rsubtree > root.data and rsubtree < root_key):
# 					rvalid = True
# 				else:
# 					rvalid = False
# 			else:
# 				rvalid = False

# 	else:
# 		if lsubtree != None:
# 			if lsubtree:
# 				if(lsubtree < root.data and lsubtree > root_key):
# 					lvalid = True
# 				else:
# 					lvalid = False
# 			else:
# 				lvalid = False
# 		if rsubtree != None:
# 			if rsubtree:
# 				if(rsubtree > root.data and rsubtree > root_key):
# 					rvalid = True
# 				else:
# 					rvalid = False
# 			else:
# 				rvalid = False

# 	if (lvalid and rvalid) or (lvalid == None and rvalid) or (rvalid == None and lvalid):
# 		return root.data
# 	else:
# 		return False

# def is_bstree(root):
# 	lsubtree = _is_bstree(root.lchild,root.data,True)
# 	rsubtree = _is_bstree(root.rchild,root.data,False)
# 	if lsubtree and rsubtree:
# 		if lsubtree < root.data and rsubtree > root.data:
# 			return True
# 	return False

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
	n9 = t.make_node(18)
	n1.lchild = n2
	n1.rchild = n3
	n2.lchild = n4
	n2.rchild = n5
	n3.lchild = n6
	n3.rchild = n7
	n5.rchild = n8
	n7.rchild = n9
	global last_seen

	is_bstree(t.root)
	print(True if last_seen else False)

if __name__ == '__main__':
	main()