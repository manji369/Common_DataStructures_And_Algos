def isComplete(grid):
  for i in range(9):
    for j in range(9):
      if grid[i][j] == '.':
        return False
  return True

def sudoku_solve(grid):
  if isComplete(grid):
      if isValid(grid):
        return True
      else:
          return False
  if not isValid(grid):
      return False
  for i in range(9):
    for j in range(9):
      if grid[i][j] == '.':
        for k in range(1, 10):
          grid[i][j] = str(k)
          if sudoku_solve(grid):
            return True
          grid[i][j] = '.'
  return False


def isValid(grid):
  for i in range(9):
    for j in range(9):
      stC = set([str(x) for x in range(1, 10)])
      for k in range(9):
        if grid[i][k] != '.':
          if grid[i][k] in stC:
            stC.remove(grid[i][k])
          else:
            return False
      stR = set([str(x) for x in range(1, 10)])
      for k in range(9):
        if grid[k][j] != '.':
          if grid[k][j] in stR:
            stR.remove(grid[k][j])
          else:
            return False
      stB = set([str(x) for x in range(1, 10)])
      for k in range(9):
        leftI, leftJ = i//3, j//3
        if grid[leftI*3+ k//3][leftJ*3 + k%3] != '.':
          if grid[leftI*3+ k//3][leftJ*3 + k%3] in stB:
            stB.remove(grid[leftI*3+ k//3][leftJ*3 + k%3])
          else:
            return False
      if stC or stR or stB:
        continue
      else:
        return False
  return True

grid = [['.' for x in range(9)] for y in range(9)]
grid[0][0] = '1'
print(sudoku_solve(grid))