# Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the
# intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
# kth node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.

from singly_linked_list import Linked_list

def intersection(lst1, lst2):

	'''
	Time Complexity : O(m+n)
	Space Complexity : O(1)
	 
	'''
	diff = abs(len(lst1) - len(lst2))

	if len(lst2)>len(lst1):
		lst1, lst2 = lst2, lst1
	head1 = lst1.get_head()
	head2 = lst2.get_head()
	last1 = None;last2 = None

	while(head1 != None):
		if head1.get_next() == None:
			last1 = head1
		head1 = head1.get_next()

	while(head2 != None):
		if head2.get_next() == None:
			last2 = head2
		head2 = head2.get_next()

	if last1.get_data() != last2.get_data():
		return False

	head1 = lst1.get_head()
	head2 = lst2.get_head()

	for _ in range(diff):
		head1 = head1.get_next()

	intersecting_node = None
	consecutive = False
	while(head1 != None):
		if head1.get_data() == head2.get_data():
			if not consecutive:
				intersecting_node = head1
				consecutive = True
		else:
			consecutive = False
		head1 = head1.get_next()
		head2 = head2.get_next()

	return intersecting_node.get_data()

def main():
	lst1 = Linked_list()
	lst1.append(1)
	lst1.append(6)
	lst1.append(9)
	lst1.append(8)
	lst1.append(2)
	lst1.append(3)
	lst1.append(10)
	lst1.append(11)

	lst2 = Linked_list()
	lst2.append(13)
	lst2.append(4)
	lst2.append(3)
	lst2.append(10)
	lst2.append(11)

	print("Input List1:")
	[print(n, end=" ") for n in lst1]
	print("\n")
	print("Input List2:")
	[print(n, end=" ") for n in lst2]
	print("\n")
	print(intersection(lst1,lst2))

if __name__ == '__main__':
	main()
