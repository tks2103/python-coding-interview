class HashRecord:
  def __init__(self, key, entry):
    self.key    = key
    self.entry  = entry

  def getKey(self):
    return self.key

  def getValue(self):
    return self.entry


class Hash:
  def __init__(self):
    self.length   = 10
    self.table    = [None] * self.length

  def hash(self, key):
    return key % self.length

  def get(self, key):
    hash_val = self.hash(key)
    if(self.has_key_collided(hash_val)):
      element = [x for x in self.table[hash_val] if x.key == key]
      if(len(element) != 1):
        raise Exception('error with collided keys')
      else:
        return element[0].getValue()
    else:
      return self.table[hash_val].getValue()

  def put(self, key, value):
    hash_val = self.hash(key)
    record = HashRecord(key, value)
    if(self.collides(hash_val)):
      self.resolve_collision(hash_val, record)
    else:
      self.table[hash_val] = record

  def collides(self, hash_val):
    return self.table[hash_val] != None

  def resolve_collision(self, hash_val, record):
    if(not self.has_key_collided(hash_val)):
      if(self.table[hash_val].key == record.key):
        self.table[hash_val] = record
        return
      else:
        self.table[hash_val] = [self.table[hash_val]]
    self.table[hash_val].append(record)

  def has_key_collided(self, hash_val):
    return isinstance(self.table[hash_val], list)

hh = Hash()
print(hh.table)
hh.put(10, 20)
print(hh.table)
print(hh.get(10))
hh.put(10, 22)
hh.put(20, 22)
print(hh.table)
print(hh.get(10))
