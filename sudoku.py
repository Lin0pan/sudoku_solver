import time

#sudoku_start = [0, 0, 3, 0, 0, 0, 8, 0, 5, 6, 0, 5, 0, 9, 0, 0, 0, 7, 0, 0, 7, 0, 4, 0, 3, 0, 0, \
#5, 6, 0, 0, 0, 0, 7, 8, 0, 0, 0, 4, 6, 7, 2, 0, 0, 9, 3, 0, 0, 0, 0, 0, 1, 4, 6, \
#4, 2, 6, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 1, 4, 0, 0, 0, 8, 0, 0, 0, 7, 0]

sudoku_start = [3, 0, 7, 1, 9, 0, 0, 0, 0, 0, 0, 0, 7, 3, 0, 1, 0, 0, 8, 0, 0, 0, 4, 2, 7, 6, 0, \
6, 0, 5, 0, 0, 4, 0, 0, 0, 0, 0, 2, 0, 0, 0, 4, 3, 8, 0, 0, 0, 8, 7, 1, 0, 0, 0, \
0, 2, 0, 9, 0, 0, 0, 1, 0, 0, 0, 6, 4, 8, 7, 0, 0, 0, 0, 4, 0, 0, 0, 0, 6, 8, 7]

d = 9
field = [[0 for x in range(d)] for y in range(d)]

def print_sudoku(field):
    for i in field:
        for j in i:
            print j, " ",
        print ""

def init_field(field, sudoku_start):
    d = len(field)
    j = 0
    i = 0
    for x in range(len(sudoku_start)):
        i = x % d
        if(x > 0 and x % 9 == 0):
            j+=1
        field[j][i] = sudoku_start[x]

    print "Initial Sudoku:"
    print_sudoku(field)


def valid(field):
    #check lines
    for j in range(d):
        for i in range(d-1):
            x = field[j][i]
            if (x in field[j][i+1:] and not x == 0):
                #print "invalid"
                return False
    #check columns
    for j in range(d):
        line = []
        for i in range(d):
            line.append(field[i][j])
        for i in range(d):
            x = line[i]
            if(x in line[i+1:] and not x == 0):
                #print "invalid"
                return False
    
    #check 3x3 cells
    line = []
    for o in range(3):
        for j in range(d):
            for i in range(3):
                y = j
                x = (i+(o*3))
                line.append(field[x][y])
    for j in range(d):
        a = j * 9
        b = (j * 9) + 9
        cell = line[a:b]
        for i in range(d):
            x = cell[i]
            if(x in cell[i+1:] and not x == 0):
                return False
   #print "valid"
    return True

def next_zero(field):
    for i in range(d):
        for j in range(d):
            if field[i][j] == 0:
                return i, j
    return -1, -1

def backtracking(solution, field):
    for i in (range(d+1)[1:]):
        nz = next_zero(field)
        x = nz[0]
        y = nz[1]
        if(x == -1 or y == -1):
            return False
        field[x][y] = i
        solution.append(i)
        if valid(field):
            nz = next_zero(field)
            if len(solution) == sudoku_start.count(0):
                print "solution found: "
                print_sudoku(field)
                print "with solution vector: "
                print solution
                return True
            
            if backtracking(solution, field):
                return True

        field[x][y] = 0
        solution.pop()
    return False

def sudoku(field, sudoku_start):
    init_field(field, sudoku_start)
    valid(field)
    solution = []
    s = time.time()
    backtracking(solution, field)
    e = time.time()
    print("time: "), (e - s)

sudoku(field, sudoku_start)