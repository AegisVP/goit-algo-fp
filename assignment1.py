from copy import deepcopy
from linked_list import LinkedList, Node


def reverse_linked_list(list: LinkedList) -> LinkedList:
    org_list = deepcopy(list)
    ret_list = LinkedList()

    while org_list.head:
        ret_list.insert_at_beginning(org_list.head.data)
        if org_list.head.next:
            org_list.head = org_list.head.next
        else:
            org_list.head = None

    return ret_list


def sort_linked_list(list):
    org_list = deepcopy(list)
    ret_list = LinkedList()

    for _ in range(org_list.len):
        cur_node = org_list.head
        largest_val = cur_node.data

        while cur_node.next:
            if largest_val < cur_node.next.data:
                largest_val = cur_node.next.data
            cur_node = cur_node.next

        org_list.delete_node(largest_val)
        ret_list.insert_at_beginning(largest_val)

    return ret_list


def join_sorted_lists(list_a, list_b):
    list1 = deepcopy(list_a)
    list2 = deepcopy(list_b)
    ret_list = LinkedList()

    while list1.head and list2.head:
        if list1.head.data < list2.head.data:
            ret_list.insert_at_end(list1.head.data)
            list1.head = list1.head.next
        else:
            ret_list.insert_at_end(list2.head.data)
            list2.head = list2.head.next

    while list1.head:
        ret_list.insert_at_end(list1.head.data)
        list1.head = list1.head.next

    while list2.head:
        ret_list.insert_at_end(list2.head.data)
        list2.head = list2.head.next

    return ret_list


if __name__ == "__main__":
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(11)
    llist.insert_at_beginning(15)

    # Вставляємо вузли в кінець
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    # Друк зв'язного списку
    print("Зв'язний список:")
    llist.print_list()

    # Друк перевернутого зв'язного списку
    rlist = reverse_linked_list(llist)
    print('\nreversed:')
    rlist.print_list()

    # Друк сортованого зв'язного списку
    slist = sort_linked_list(llist)
    print()
    print('\nsorted:')
    slist.print_list()

    # Друк поєднаного зв'язного списку
    llist2 = LinkedList()
    llist2.insert_at_end(2)
    llist2.insert_at_end(3)
    llist2.insert_at_end(14)
    llist2.insert_at_end(22)
    llist2.insert_at_end(23)
    llist2.insert_at_end(24)
    llist2.insert_at_end(35)

    print('\nlist2:')
    llist2.print_list()

    jlist = join_sorted_lists(slist, llist2)
    print()
    print('\njoined:')
    jlist.print_list()
