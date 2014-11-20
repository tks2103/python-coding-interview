from linked_list import LinkedList, Node

def partition_list(num, lst):
  smaller = LinkedList(None)
  bigger = LinkedList(None)

  current = lst.root
  while current:
    print('hi')
    print(current.data <= num)
    smaller.insert_at_end(Node(None, current.data)) if current.data <= num else bigger.insert_at_end(Node(None, current.data))
    current = current.next

  smaller.insert_at_end(bigger.root)
  return smaller

lst = LinkedList.build_from_array([3, 4, 7, 2, 6, 1, 5, 8, 9, 5])
lst.prn()
partition_list(5, lst).prn()
