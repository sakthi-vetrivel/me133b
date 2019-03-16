import numpy as np
import sys

size = 10
obstacles = []
visited = []
workspace = [["0" for x in range(size)] for y in range(size)]
goal,init = (0,0)
path = []

# function to create n random obstacles in the workspace
def create_obstacles(n):
    for i in range(n):
        w = np.random.randint(1, size/2)
        h = np.random.randint(1, size/2)
        x = np.random.randint(0, size)
        y = np.random.randint(0,size)
        obstacles.append((w,h,x,y))

# Add obstacles once they have been created to the workspace
def add_obstacles():
    for o in obstacles:
        x = o[2]
        y = o[3]
        for i in range(o[0]):
            for j in range(o[1]):
                if (i + x < size and j + y < size):
                    workspace[i + x][j + y] = "1"

# print a visualization of the workspace
def print_w():
    for i in range (0, size):
        print(workspace[i])
    print("\n")

# set the goal for the robot
def set_goal():
    goal = (size - 1, size - 1)
    workspace[goal[0]][goal[1]] = "2"

# set the initial position for the robot
def set_init():
    init = (0,0)
    workspace[init[0]][init[1]] = "0"

# Set the value of a cell
def get_min(i, j, min):
    if i >= 0 and i <= size-1 and j >= 0 and j <=size-1:
        if(workspace[i][j] == "0" or workspace[i][j] == "1"):
            return min
        if (int(workspace[i][j]) < min):
            return int(workspace[i][j])
    return min

# Push a cell onto the visited queue
def push_visited(i, j):
    if (i >= 0 and i <= size-1 and j >= 0 and j <=size-1 and workspace[i][j] == "0"):
        visited.append((i,j))

def push_adj(x, y):
    push_visited(x+1, y)
    push_visited(x+1, y+1)
    push_visited(x+1, y-1)
    push_visited(x-1, y)
    push_visited(x-1, y+1)
    push_visited(x-1, y-1)
    push_visited(x, y+1)
    push_visited(x, y-1)

# Set all of the adjacent cells to value
def set_adj(x, y, value):
    value = str(value)
    set(x+1, y, value)
    set(x-1, y, value)
    set(x, y+1, value)
    set(x, y-1, value)
    set(x+1, y+1, value)
    set(x-1, y+1, value)
    set(x+1, y-1, value)
    set(x-1, y-1, value)

def get_min_of_neighbors(x, y):
    min = size*size
    min = get_min(x+1, y, min)
    min = get_min(x-1, y, min)
    min = get_min(x+1, y-1, min)
    min = get_min(x-1, y-1, min)
    min = get_min(x+1, y+1, min)
    min = get_min(x-1, y+1, min)
    min = get_min(x, y+1, min)
    min = get_min(x, y-1, min)

    if (min == size*size):
        return None
    return min


def label_cells():
    # Add all zero labels to queue
    visited.append((size-1,size-1))
    push_adj(size-1, size-1)

    # While loop to set all values
    i = 0
    while len(visited) != 0:
        # Get the first point
        point = visited.pop(0)
        x = point[0]
        y = point[1]
        min = get_min_of_neighbors(x,y)
        if (min != None):
            workspace[x][y] = str(int(min) + 1)
        push_adj(x, y)
        i = i +1

    print_w()

def check(i, j, value, n):
    if (i >= 0 and i <= size-1 and j >= 0 and j <=size-1 and workspace[i][j] == str(value)):
        n.append((i,j))


def find_lower_neighbor(x, y, value):
    n = []
    check(x + 1, y, value - 1, n)
    check(x - 1, y, value - 1, n)
    check(x, y + 1, value - 1, n)
    check(x, y - 1, value - 1, n)
    check(x - 1, y + 1, value - 1, n)
    check(x - 1, y - 1, value - 1, n)
    check(x + 1, y + 1, value - 1, n)
    check(x + 1, y - 1, value - 1, n)
    return n


def find_path():
    x = 0
    y = 0
    while((x,y) != (size - 1, size - 1)):
        path.append((x,y))
        options = find_lower_neighbor(x,y, int(workspace[x][y]))
        i = np.random.randint(len(options))
        x = options[i][0]
        y = options[i][1]
    path.append((size - 1, size - 1))

create_obstacles(4)
add_obstacles()
set_goal()
set_init()
print_w()
label_cells()

if (workspace[0][0] != "0"):
    print("There's a path from init to the goal!")
    find_path()
    print(path)
    # This is where the visualization should happen
else:
    print("There is no path from init to the goal")
