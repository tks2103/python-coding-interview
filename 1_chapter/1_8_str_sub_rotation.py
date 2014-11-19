def is_substring(str1, str2):
  return str1 in str2

def is_rotation(str1, str2):
  if len(str1) != len(str2):
    return False
  for i in range(1,len(str2)-1):
    if is_substring(str1[i:], str2) and is_substring(str1[:i], str2):
      return True
  return False

assert(is_rotation("abc", "bca") == True)
assert(is_rotation("abc", "baca") == False)
assert(is_rotation("abca", "baca") == False)
