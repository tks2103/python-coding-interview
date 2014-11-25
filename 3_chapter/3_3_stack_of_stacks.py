from stack import Stack

class SetOfStacks():
  def __init__(self, capacity):
    self.capacity = capacity
    self.stacks = []

  def get_last_stack(self):
    if len(self.stacks) == 0:
      return None
    else:
      return self.stacks[-1]

  def push(self, data):
    stack = self.get_last_stack()
    if stack:
      if stack.size == self.capacity:
        self.stacks.append(Stack())
        self.push(data)
      else:
        stack.push(data)
    else:
      self.stacks.append(Stack())
      self.push(data)

  def pop(self):
    stack = self.get_last_stack()
    if stack:
      if stack.size == 0:
        self.stacks.pop()
        return self.pop()
      else:
        return stack.pop()

  def pop_at(self, index):
    if index < len(self.stacks):
      return self.stacks[index].pop()



ss = SetOfStacks(2)
ss.push(3)
ss.push(4)
ss.push(5)
assert(len(ss.stacks) == 2)
assert(ss.pop() == 5)
assert(ss.pop() == 4)
assert(len(ss.stacks) == 1)
assert(ss.pop() == 3)

ss.push(3)
ss.push(4)
ss.push(5)
assert(len(ss.stacks) == 2)
assert(ss.pop_at(0) == 4)
assert(ss.pop_at(0) == 3)
assert(ss.pop_at(0) == None)
assert(ss.pop() == 5)
assert(ss.pop() == None)
