
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

solution = [[5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]]

def is_valid(grid, x, y, i):
    # check columns
    for cell in range(0, 9):
        if grid[x][cell] == i:
            return False
    # check rows
    for cell in range(0, 9):
        if grid[cell][y] == i:
            return False
    return True

def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    for x in range(0,9):
        for y in range(0, 9):
            if puzzle[x][y] == 0: # cell is empty
                i = 0
                while i <= 9:
                    valid = is_valid(puzzle, x, y, i)
                    print "is_valid(grid, %s, %s, %s) is %s" % (x, y, i, valid)
                    if valid:
                        puzzle[x][y] = i
                        break
                    else:
                        i += 1
    return puzzle

soln = sudoku(puzzle)

print "Original:"
for row in puzzle:
    print row

print "Your solution:"
for row in soln:
    print row

print "The real solution:"
for row in solution:
    print row
    
if soln == solution:
    print "Success"
