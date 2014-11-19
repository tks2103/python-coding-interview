class Node:
  def __init__(self, n, d):
    self.next = n
    self.data = d

class LinkedList:
  def __init__(self, r):
    self.root = r

  def insertAtEnd(self, n):
    if self.root == None:
      self.root = n
      return
    current = self.root
    while current.next != None:
      current = current.next
    current.next = n

  @staticmethod
  def buildFromArray(ary):
    new_list = LinkedList(None)
    for x in ary:
      add = Node(None, x)
      new_list.insertAtEnd(add)
    return new_list

lst = LinkedList.buildFromArray([1,3,2])

if __name__ == "__main__":
  assert(lst.root.data == 1)
  assert(lst.root.next.data == 3)
  assert(lst.root.next.next.data == 2)