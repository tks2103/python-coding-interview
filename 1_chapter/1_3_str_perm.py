def get_signature(input_string):
  hsh = {}
  for c in input_string:
    if not c in hsh:
      hsh[c] = 0
    hsh[c] += 1
  return hsh

def is_perm(str1, str2):
  sig1 = get_signature(str1)
  sig2 = get_signature(str2)
  return sig1 == sig2

assert(get_signature("abc") == { 'a': 1, 'b': 1, 'c': 1})
assert(is_perm("acb", "abc") == True)
assert(is_perm("cb", "abc") == False)
