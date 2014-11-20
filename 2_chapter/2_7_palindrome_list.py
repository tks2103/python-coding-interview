from linked_list import LinkedList, Node

def reverse_list(lst):
  node = Node(None, lst.root.data)
  current = lst.root.next
  while current:
    node = Node(node, current.data)
    current = current.next

  return LinkedList(node)

def check_palindrome(lst):
  lst2 = reverse_list(lst)
  current1 = lst.root
  current2 = lst2.root

  while current1 and current2:
    if current1.data != current2.data:
      return False
    current1 = current1.next
    current2 = current2.next
  return True

lst1 = LinkedList.build_from_array([1,2,3,2,1])
lst2 = LinkedList.build_from_array([1,2,3,1,1])

print(check_palindrome(lst1))
print(check_palindrome(lst2))
