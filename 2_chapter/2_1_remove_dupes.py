from linked_list import LinkedList

def remove_dupes(lst):
  hsh = {}
  previous = lst.root
  current = lst.root
  while current:
    if current.data in hsh:
      previous.next = current.next
    else:
      hsh[current.data] = True
      previous = current
    current = current.next

def remove_dupes_in_place(lst):
  current = lst.root
  while current:
    runner = current.next
    previous = current
    while runner:
      if runner.data == current.data:
        previous.next = runner.next
      else:
        previous = previous.next
      runner = runner.next
    current = current.next

lst = LinkedList.build_from_array(['F', 'O', 'L', 'L', 'O', 'W', 'U', 'P'])
lst.prn()
remove_dupes_in_place(lst)
lst.prn()
lst = LinkedList.build_from_array(['F', 'O', 'L', 'L', 'O', 'W', 'U', 'P'])
remove_dupes(lst)
lst.prn()
