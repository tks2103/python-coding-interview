from linked_list import LinkedList

def remove_kth_last_element(k, lst):
  if k <= 0:
    return
  current = lst.root
  runner = lst.root
  i = 0
  while runner and i < k:
    runner = runner.next
    i += 1

  if i != k:
    raise Exception("Linked List too small")

  if not runner:
    lst.root = lst.root.next
    return

  previous = current
  while runner:
    previous = current
    current = current.next
    runner = runner.next

  previous.next = current.next

lst = LinkedList.build_from_array([1, 2, 3])
lst.prn()
remove_kth_last_element(0, lst)
lst.prn()
