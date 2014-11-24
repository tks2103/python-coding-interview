class Node(object):
  def __init__(self, data): 
    self.next = None
    self.data = data

class Stack(object):
  def __init__(self):
    self.top = None
    self.size = 0

  def push(self, data):
    node = Node(data)
    node.next = self.top
    self.top = node
    self.size += 1

  def pop(self):
    if(self.top != None):
      item = self.top.data
      self.top = self.top.next
      self.size -= 1
      return item
    return None

  def peek(self):
    if not self.top:
      raise Exception('Empty Stack')
    return self.top.data

if __name__ == '__main__':
  stack = Stack()
  stack.push(3)
  stack.push(2)
  assert(stack.top.data == 2)
  assert(stack.top.next.data == 3)
  assert(stack.pop() == 2)
  assert(stack.peek() == 3)
  assert(stack.pop() == 3)
  #stack.peek()
  assert(stack.pop() == None)
