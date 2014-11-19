from linked_list import LinkedList

lst = LinkedList.build_from_array(['F', 'O', 'L', 'L', 'O', 'W', 'U', 'P'])

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

remove_dupes(lst)
lst.prn()
