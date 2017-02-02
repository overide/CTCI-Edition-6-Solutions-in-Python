# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

from singly_linked_list import Linked_list

def kth_last(lst, k):
	'''
	Time Complexity : O(n)
	Space Complexity : O(1)
	'''
	head = lst.get_head()
	nodes_count = 0

	while(head != None): #O(n)
		nodes_count += 1
		head = head.get_next()

	head = lst.get_head()
	m = (nodes_count-k)
	nodes_count = 0

	while(nodes_count <= m): #O(m)
		nodes_count += 1
		if nodes_count == m:
			return head.get_data()
		head = head.get_next()

def main():
    lst = Linked_list()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.append(4)
    lst.append(5)
    lst.append(6)
    print("Our list:\n")
    [print(n, end=" ") for n in lst]
    k = int(input("\nEnter Kth element:"))
    print("\nKth last node is:{}".format(kth_last(lst,k)))

if __name__ == '__main__':
    main()
