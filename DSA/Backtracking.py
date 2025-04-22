''''
BLUEPRINT
example of sudoku solver
Choice

Constraints

Goals

'''









def count_path(r,c):
    if r == 1 or c == 1:
        return 1
    left = count_path(r-1,c)
    right = count_path(r,c-1)
    return left+right

print(count_path(3,3))


def print_path(path,r,c):
    if r == 1 and c == 1:

        return [path]
    li = []
    if r > 1:
        li.extend(print_path(path+'D',r-1,c))
    if c > 1:
        li.extend(print_path(path+"R",r,c-1))
    # if r > 1 and c > 1:
    #     li.extend(print_path(path+"d",r-1,c-1))
    return li
print(print_path("",3,3))

def pathObstacle(path,maze,r,c):
    if r == len(maze) - 1 and c == len(maze[0]) - 1:
        return [path]

    if maze[r][c] == 0:
        return [None]
    li = []
    if r < len(maze) - 1:
        li.extend(pathObstacle(path+'D',maze,r+1,c))
    if c < len(maze[0]) - 1:
        li.extend(pathObstacle(path+"R",maze,r,c+1))
    return li
maze = [[1,1,1],[1,0,1],[1,1,1]]
print(pathObstacle("",maze,0,0))


