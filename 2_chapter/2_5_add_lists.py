from linked_list import LinkedList, Node
import math

def add_lists_reverse(lst1, lst2):
  accumulator = 0
  current1 = lst1.root
  current2 = lst2.root
  output   = LinkedList(None)
  while current1 and current2:
    value = current1.data + current2.data + accumulator
    accumulator = int(math.floor(value / 10))
    output.insert_at_end(Node(None, value % 10))
    current1 = current1.next
    current2 = current2.next
  if current1:
    value = current1.data + accumulator
    output.insert_at_end(Node(None, value % 10))
    if value > 10:
      output.insert_at_end(Node(None, int(math.floor(value/10))))
  elif current2:
    value = current2.data + accumulator
    output.insert_at_end(Node(None, value % 10))
    if value > 10:
      output.insert_at_end(Node(None, int(math.floor(value/10))))
  else:
    if accumulator > 0:
      output.insert_at_end(Node(None, accumulator))

  return output

def reverse_list(lst):
  node = Node(None, lst.root.data)
  current = lst.root.next
  while current:
    node = Node(node, current.data)
    current = current.next

  return LinkedList(node)

lst1 = LinkedList.build_from_array([5,2,5])
lst2 = LinkedList.build_from_array([1,4,8,5])

add_lists_reverse(lst1, lst2).prn()
add_lists_reverse(reverse_list(lst1), reverse_list(lst2)).prn()
