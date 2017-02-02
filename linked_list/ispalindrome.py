# Palindrome: Implement a function to check if a linked list is a palindrome.

from singly_linked_list import Linked_list,Node

def is_palindrome(lst):
	'''
	Time Complexity : O(n)
	space Complexity : O(n)
	'''
	lst2 = Linked_list()
	for e in lst:
		lst2.append(e)

	current = lst2.get_head()
	prev = None

	while(current != None):
		tmp = current.get_next()
		current.set_next(prev)
		prev = current
		current = tmp

	lst2.set_head(prev)
	
	head1 = lst.get_head()
	head2 = lst2.get_head()

	while( head1 != None):
		if head1.get_data() != head2.get_data():
			return False
		head1 = head1.get_next()
		head2 = head2.get_next()

	return True

def main():
	lst = Linked_list()
	lst.append(1)
	lst.append(1)
	lst.append(2)
	lst.append(2)
	lst.append(1)
	lst.append(1)
	print("Input List:")
	[print(n, end=" ") for n in lst]
	print("\n")
	print(is_palindrome(lst))

if __name__ == '__main__':
	main()