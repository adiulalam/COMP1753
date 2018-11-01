# draw two squares, side by side, not touching

from turtle import *


def draw_square1():
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)

def draw_square2():
    forward(110)
    left(90)
    forward(110)
    left(90)
    forward(110)
    left(90)
    forward(110)
    left(90)

def draw_square3():
    forward(120)
    left(90)
    forward(120)
    left(90)
    forward(120)
    left(90)
    forward(120)
    left(90)

def draw_square4():
    forward(130)
    left(90)
    forward(130)
    left(90)
    forward(130)
    left(90)
    forward(130)
    left(90)

draw_square1()

penup()
forward(150)
pendown()

draw_square2()

penup()
forward(150)
pendown()

draw_square3()

penup()
forward(150)
pendown()

draw_square4()

exitonclick()

print()
input("Press return to continue ...")
