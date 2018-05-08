class Grid:
    def __init__(self, 

def yield_sudoku():
    with open('p096_sudoku.txt') as f:
        f.readline()
        grid = []
        for _ in range(9):
            grid.append(f.readline())
        yield grid

for x in yield_sudoku():
    print(x)
            
