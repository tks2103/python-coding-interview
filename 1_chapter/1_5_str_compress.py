def recursive_compress(input_string, c, ct):
  if len(input_string) == 0:
    return "" + c + str(ct)
  if input_string[0] == c:
    return recursive_compress(input_string[1:], c, ct+1)
  else:
    return "" + c + str(ct) + recursive_compress(input_string[1:], input_string[0], 1)

def str_compress(input_string):
  comp_string = recursive_compress(input_string[1:], input_string[0], 1)
  if len(comp_string) >= len(input_string):
    return input_string
  return comp_string

assert(recursive_compress("aaccbbaacc", "a", 1) == "a3c2b2a2c2")
assert(str_compress("aabb") == "aabb")
assert(str_compress("aabbb") == "a2b3")
