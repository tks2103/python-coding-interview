from linked_list import LinkedList, Node
import math

def find_loop(lst):
  fast_runner = lst.root
  slow_runner = lst.root

  while fast_runner and slow_runner:
    fast_runner = fast_runner.next.next
    slow_runner = slow_runner.next
    if fast_runner == slow_runner:
      break

  slow_runner = lst.root
  while fast_runner and slow_runner:
    fast_runner = fast_runner.next
    slow_runner = slow_runner.next
    if fast_runner == slow_runner:
      return slow_runner


lst = LinkedList.build_from_array([1,2,3,4,5,6])
lst.insert_at_end(lst.root.next.next)
print(find_loop(lst).data)
