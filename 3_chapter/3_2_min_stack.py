from stack import Stack

class MinStack(Stack):

  def __init__(self):
    super(MinStack, self).__init__()
    self.min_stack = Stack()

  def push(self, data):
    Stack.push(self, data)
    if self.min_stack.top == None:
      self.min_stack.push(data)
      return
    if data <= self.min_stack.peek():
      self.min_stack.push(data)

  def pop(self):
    if self.top == None:
      return None
    item = Stack.pop(self)
    if item == self.min_stack.peek():
      self.min_stack.pop()
    return item

  def min(self):
     return self.min_stack.peek()

stack = MinStack()
stack.push(3)
assert(stack.min() == 3)
stack.push(1)
assert(stack.min() == 1)
stack.push(2)
assert(stack.min() == 1)
stack.push(0)
assert(stack.min() == 0)
stack.pop()
assert(stack.min() == 1)
