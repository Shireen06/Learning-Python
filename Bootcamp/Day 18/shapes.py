# -*- coding: utf-8 -*-

import turtle as t
from turtle import Screen
import random


tom = t.Turtle()
screen = Screen()
screen.colormode(255)

def draw_polygon(number_of_sides):
    angle = 360/number_of_sides
    
    for figure in range(number_of_sides):
        tom.pencolor(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        tom.forward(100)
        tom.right(angle)
        
for x in range(3, 11):
    draw_polygon(x)
    

# tom.pencolor("red")
# for triangle in range(3):
#     tom.forward(100)
#     tom.right(120)


# tom.pencolor("green")
# for square in range(4):
#     tom.forward(100)
#     tom.right(90)


# tom.pencolor("blue")
# for pentagon in range(5):
#     tom.forward(100)
#     tom.right(72)


# tom.pencolor("brown")
# for sextagon in range(6):
#     tom.forward(100)
#     tom.right(60)

# tom.pencolor("aquamarine")
# for septagon in range(7):
#     tom.forward(100)
#     tom.right(51.4)

# tom.pencolor("black")
# for octagon in range(8):
#     tom.forward(100)
#     tom.right(45)

# tom.pencolor("DarkGoldenrod1")
# for nonagon in range(9):
#     tom.forward(100)
#     tom.right(40)
    
    
# tom.pencolor("DarkViolet")
# for decagon in range(10):
#     tom.forward(100)
#     tom.right(36)
    



