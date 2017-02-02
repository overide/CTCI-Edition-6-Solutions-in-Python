# Delete Middle Node: Implement an algorithm to delete a node in the middle (Le., any node but
# the fi rst and last node, not necessarily the exact middle) of a singly linked list,
# GIVEN ONLY ACCESS TO NODE c ONLY.

# EXAMPLE
# Input: the node c from the linked list a - >b- >c - >d - >e- >f
# Resul t: noth ing is returned, but the new linked list looks like a -> b->d->e->f

from singly_linked_list import Linked_list

def delete_middle(n):
	nextn = n.get_next()
	n.set_data(nextn.get_data())
	n.set_next(nextn.get_next())

def main():
    lst = Linked_list()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.append(4)
    lst.append(5)
    lst.append(6)
    print("Input list:\n")
    [print(n, end=" ") for n in lst]
    node_to_del = lst.get_head().get_next().get_next()
    delete_middle(node_to_del)
    print("\nAfter deleting node 3:\n")
    [print(n, end=" ") for n in lst]
    print("\n")

if __name__ == '__main__':
    main()
