# Paths with Sum: You are given a binary tree in which each node contains an integer value (which
# might be positive or negative) . Design an algorithm to count the number of paths that sum to a
# given value. The path does not need to start or end at the root or a leaf, but it must go downwards
# (traveling only from parent nodes to child nodes).

from collections import defaultdict
from tree import Tree

def count_paths(root, key, path_dict = defaultdict(int), running_sum = 0):
	'''
	Time Complexity : O(n)
	Space Complexity : O(n)
	Space Complexity (Balanced Tree) : O(log n) 
	'''
	if root == None:return 0
	running_sum += root.data
	look_up = running_sum - key
	total_paths = path_dict.get(look_up,0)

	if running_sum == key:
		total_paths += 1

	path_dict[running_sum] += 1

	total_paths += count_paths(root.lchild, key, path_dict, running_sum)
	total_paths += count_paths(root.rchild, key, path_dict, running_sum)

	path_dict[running_sum] -= 1
	if path_dict[running_sum] == 0:
		del path_dict[running_sum]

	return total_paths

def main():

	t1 = Tree()
	n1 = t1.make_node(10)
	n2 = t1.make_node(5)
	n3 = t1.make_node(-3)
	n4 = t1.make_node(3)
	n5 = t1.make_node(2)
	n6 = t1.make_node(11)
	n7 = t1.make_node(3)
	n8 = t1.make_node(-2)
	n9 = t1.make_node(1)

	n1.lchild = n2
	n1.rchild = n3
	n2.lchild = n4
	n2.rchild = n5
	n3.rchild = n6
	n4.lchild = n7
	n4.rchild = n8
	n5.rchild = n9

	print("Number of paths sum to {} are: {}".format(8,count_paths(t1.root,8)))

if __name__ == '__main__':
	main()