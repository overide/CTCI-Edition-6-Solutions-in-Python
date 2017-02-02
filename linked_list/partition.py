# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x . lf x is contained within the list, the values of x only need
# to be after the elements less than x (see below) . The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 - > 10 -> 2 -> 1 [partition = 5)
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

from singly_linked_list import Linked_list,Node

def partition(lst,nodex):
    '''
    Time Complexity = O(N)
    Space Complexity = O(1)
    '''
    current = lst.get_head()
    prev = Node()
    if current.get_data()<nodex:
        prev = current
        current = current.get_next()

    while current != None:
        if current.get_data() < nodex:
            tmp = current
            current = current.get_next()
            prev.set_next(current)
            tmp.set_next(lst.get_head())
            lst.set_head(tmp)
        else:
            prev = current
            current = current.get_next()

def main():
    lst = Linked_list()
    lst.append(7)
    lst.append(3)
    lst.append(5)
    lst.append(8)
    lst.append(5)
    lst.append(10)
    lst.append(2)
    lst.append(1)
    print("Input List:\n")
    [print(n, end=" ") for n in lst]
    partition(lst,5)
    print("\nList after partition\n")
    [print(n, end=" ") for n in lst]

if __name__ == '__main__':
    main()