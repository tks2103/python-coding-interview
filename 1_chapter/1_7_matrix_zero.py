def get_matrix_operations(mat):
  ops = []
  for i in range(len(mat)):
    for j in range(len(mat[0])):
      if mat[i][j] == 0:
        ops.append(('row', i))
        ops.append(('col', j))
  return ops

def process_ops(mat, ops):
  for x in ops:
    i = x[1]
    if x[0] == 'row':
      for j in range(len(mat[0])):
        mat[i][j] = 0
    else:
      for j in range(len(mat)):
        mat[j][i] = 0

  return mat

def matrix_zero(mat):
  ops = get_matrix_operations(mat)
  mat = process_ops(mat, ops)
  return mat

mat = [ [4,4,4,4],
        [4,0,4,4],
        [4,4,0,4],
        [4,4,4,4] ]
assert(get_matrix_operations(mat) == [('row', 1), ('col', 1), ('row', 2), ('col', 2)])
assert(process_ops(mat, [('row', 1)]) == [[4,4,4,4],[0,0,0,0],[4,4,0,4],[4,4,4,4]])
assert(process_ops(mat, [('col', 1)]) == [[4,0,4,4],[0,0,0,0],[4,0,0,4],[4,0,4,4]])
mat = [ [4,4,4,4],
        [4,0,4,4],
        [4,4,0,4],
        [4,4,4,4] ]
assert(matrix_zero(mat) == [[4,0,0,4],[0,0,0,0],[0,0,0,0],[4,0,0,4]])
