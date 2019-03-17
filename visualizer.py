from turtle import *

def create_world(size):
    screen = getscreen()
    setworldcoordinates(0, size - 1, size - 1, 0)
    setpos(0,0)

def draw_obstacles(obstacles):
    speed(10)
    color('red', 'yellow')

    for o in obstacles:
        h = o[0]
        w = o[1]
        y = o[2] - 1
        x = o[3] - 1
        up()
        begin_fill()
        setpos(x,y)
        print(pos())
        down()
        forward(w)
        print(pos())
        left(90)
        forward(h)
        print(pos())
        left(90)
        forward(w)
        print(pos())
        left(90)
        forward(h)
        print(pos())
        left(90)
        end_fill()

def draw_path(path):
    speed(1)
    up()
    setpos(0,0)
    down()
    pensize(10)
    for (x,y) in path:
        goto(y,x)
