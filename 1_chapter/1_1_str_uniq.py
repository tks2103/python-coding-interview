from sets import Set

def detect_uniq(input_string):
  st = Set()
  for c in input_string:
    if c in st:
      return False
    st.add(c)
  return True

assert(detect_uniq("abc") == True)
assert(detect_uniq("abb") == False)
