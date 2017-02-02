# Remove Dups: Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

from singly_linked_list import Linked_list

def remove(lst):
	'''
	Time complexity : O(N)
	Space Complexity : O(N) 
	'''
	head = lst.get_head()
	seen = []
	while(head != None):
		try:
			if head.get_next().get_data() in seen:
				head.set_next(head.get_next().get_next())

		except AttributeError as e:
			pass
		seen.append(head.get_data())
		head = head.get_next()
	return lst

def remove_no_buffer(lst):
	'''
	Time Complexity : O(N^2)
	Space Complexity : O(1)
	'''
	p1 = lst.get_head()
	while(p1 != None):
		p2 = p1.get_next()
		while(p2 != None):
			try:
				if p2.get_next().get_data() == p1.get_data():
					p2.set_next(p2.get_next().get_next())
			except AttributeError as e:
				pass
			p2 = p2.get_next()
		p1 = p1.get_next()

	return lst

def main():
    lst = Linked_list()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.append(2)
    lst.append(5)
    lst.append(3)
    print("list with duplicates:\n")
    [print(n, end=" ") for n in lst]
    print("\n")
    remove_no_buffer(lst)
    print("\nList without duplicates\n")
    [print(n, end=" ") for n in lst]
    print("\n")

if __name__ == '__main__':
    main()