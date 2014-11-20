from linked_list import LinkedList

def delete_in_middle(node):
  if not node.next:
    return

  node.data = node.next.data
  node.next = node.next.next

lst = LinkedList.build_from_array([1, 2, 3, 4])
lst.prn()
delete_in_middle(lst.root.next.next)
lst.prn()
