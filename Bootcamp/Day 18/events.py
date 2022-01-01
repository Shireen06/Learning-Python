# -*- coding: utf-8 -*-
from turtle import Turtle, Screen

Tommy = Turtle()
screen = Screen()

def move_forwards():
    Tommy.forward(10)

def move_backwards():
    Tommy.back(10)
    
def move_cc():
    Tommy.left(90)
    
def move_cw():
    Tommy.right(90)
    
def clear():
    Tommy.clear()
    Tommy.penup()
    Tommy.home()
    Tommy.pendown()

screen.listen()
screen.onkey(key= "w", fun=move_forwards)
screen.onkey(key= "s", fun=move_backwards)
screen.onkey(key= "a", fun=move_cc)
screen.onkey(key= "d", fun=move_cw)    
screen.onkey(key= "c", fun=clear)
screen.exitonclick()