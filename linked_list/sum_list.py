# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7-) 1 -) 6) + (5 -) 9 -) 2) .Thatis,617 + 295.
# Output: 2 -) 1 -) 9. That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# Input: (6 -) 1 -) 7) + (2 -) 9 -) 5) . Thatis,617 + 295 .
# Output: 9 -) 1 -) 2. That is, 912.

from singly_linked_list import Linked_list,Node

def add(lst1,lst2):
    '''
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    if len(lst1) >= len(lst2):
        lst1, lst2 = lst1, lst2
    else:
        lst1, lst2 = lst2, lst1
    head1 = lst1.get_head()
    head2 = lst2.get_head()
    carry=0

    while(head1 != None or head2 != None):
        if head1 and head2:
            val = head1.get_data() + head2.get_data()
            if head1.get_next() != None and head2.get_next() != None:
                head1.set_data((val + carry)%10)
            else:
                head1.set_data((val + carry) % 10)
                if (val + carry) > 10:
                    lst1.append((val + carry) // 10)
                break
            carry = val//10
            head1 = head1.get_next()
            head2 = head2.get_next()

        else:
            val = head1.get_data()
            if head1.get_next() != None:
                head1.set_data((val + carry)%10)
            else:
                head1.set_data((val + carry)%10)
                if (val + carry) > 10:
                    lst1.append((val + carry) // 10)
                break

            carry = val//10
            head1 = head1.get_next()

def _sum(ptr1, ptr2):
    if ptr1.get_next() == None and ptr2.get_next() == None:
        val = ptr1.get_data() + ptr2.get_data()
        ptr1.set_data(val % 10)
        return (val // 10)

    carry = _sum(ptr1.get_next(), ptr2.get_next())
    val = ptr1.get_data() + ptr2.get_data()+carry
    ptr1.set_data(val % 10)
    return val // 10

def add_followup(lst1, lst2):
    if len(lst1)<len(lst2):
        lst1, lst2 = lst2, lst1
    for _ in range(len(lst1) - len(lst2)):
        h = lst2.get_head()
        n = Node(0)
        n.set_next(h)
        lst2.set_head(n)

    _sum(lst1.get_head(),lst2.get_head())

def main():
    lst1 = Linked_list()
    lst2 = Linked_list()

    lst1.append(6)
    lst1.append(1)
    lst1.append(7)
    lst2.append(2)
    lst2.append(9)
    # lst2.append(5)

    print("Input List1:")
    [print(n, end=" ") for n in lst1]
    print("\n")
    print("Input List2:")
    [print(n, end=" ") for n in lst2]

    add_followup(lst1,lst2)
    
    print("\nSummed List:")
    [print(n, end=" ") for n in lst1]
    print("\n")

if __name__ == '__main__':
    main()