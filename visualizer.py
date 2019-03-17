from turtle import *

def create_world(size):
    screen = getscreen()
    setworldcoordinates(0, size - 1, size - 1, 0)
    setpos(0,0)

def draw_obstacles(obstacles):
    color('red', 'yellow')

    for o in obstacles:
        print(pos())
        h = o[0] + 1
        w = o[1]
        y = o[2] + 1
        x = o[3]
        up()
        begin_fill()
        setpos(x,y)
        down()
        forward(w)
        print(pos())
        right(90)
        forward(h)
        print(pos())
        right(90)
        forward(w)
        print(pos())
        right(90)
        forward(h)
        print(pos())
        right(90)
        end_fill()

def draw_path(path):
    speed(1)
    up()
    setpos(0,0)
    down()
    pensize(10)
    for (x,y) in path:
        print(x,y)
        goto(x,y)
