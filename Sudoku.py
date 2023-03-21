import numpy as np

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,3,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,0,0]]


print (np.matrix(grid))

def possible(row,col,num):

    global grid
    # is the number appearing in the the row ?
    for i in range(0,9):
        if grid[row][i] == num:
            return False
    # is the number appearing in the the column ?
    for i in range(0,9):
        if grid[i][col] == num:
            return False
    # is the number appearing in the the given square ? 
    x0 = (row//3)*3
    y0 = (col//3)*3

    for i in range(0,3):
        for j in range(0,3):
            if grid[x0+i][y0+j] == num:
                return False

    return True


def solve():
    global grid
    for row in range(0,9):
        for col in range(0,9):
            if grid[row][col] == 0:
                for number in range(1,10):
                    if possible(row,col,number):
                        grid[row][col] = number
                        solve()
                        grid[row][col] = 0

                return
    
    print("")
    print(np.matrix(grid))
    print("")
    print("Alternate Solutions")

    
solve()        

