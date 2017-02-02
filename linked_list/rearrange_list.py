# suppose you had a linked list a1 - > a2 - > ••• - >an - >b1 - >b2 - > ••• - >bn and you wanted to
# rearrange it into a1 - >b1 - >a2 - >b2 - > ••• - >an - >bn You do not know the length of the linked list (but you
# do know that the length is an even number)

from singly_linked_list import Linked_list


def rearrange(lst):
    slow = lst.get_head()
    fast = lst.get_head()

    while(fast != None):
        slow = slow.get_next()
        fast = fast.get_next().get_next().get_next()

    fast = lst.get_head()
    while(slow != fast):
        tmp_node = slow.get_next()
        slow.set_next(tmp_node.get_next())
        tmp_node.set_next(fast.get_next())
        fast.set_next(tmp_node)
        fast = fast.get_next().get_next()

    return lst


def main():
    lst = Linked_list()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.append(4)
    lst.append(5)
    lst.append(6)
    print("list before reorder:\n")
    [print(n, end=" ") for n in lst]
    rearrange(lst)
    print("\nList after rearrangement\n")
    [print(n, end=" ") for n in lst]

if __name__ == '__main__':
    main()
