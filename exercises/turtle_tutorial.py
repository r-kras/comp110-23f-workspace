"""Learning how to use turtle."""

__author__ = "730699792"

# Importing and Setting Up the Turtle
from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

# Lines and turning

def square():
    """Making a square with Turtle."""
    leo.left(90)
    leo.forward(100)
    leo.left(90)
    leo.forward(100)
    leo.left(90)
    leo.forward(100)
    leo.left(90)
    leo.forward(100)


def square_loop(side_length: int):
    """EX1: Making a square with Loops and Turtle."""
    for i in range(0, 4):
        leo.left(90)
        leo.forward(side_length)


def triangle_loop(side_length: int):
    """EX2: Making a triangle with Loops and Turtle."""
    for i in range(0, 3):
        leo.left(120)
        leo.forward(side_length)


def triangle_fill(side_length: int):
    # "white" = 0, 0, 0
    # "black" = 255, 255, 255
    # "grey" = 123, 123, 123
    # "red" = 255, 0, 0
    colormode(255)
    leo.speed(100)
    leo.hideturtle()
    leo.penup()
    leo.goto(45, 60)
    leo.pendown()
    leo.fillcolor(255, 0, 0)
    leo.begin_fill()
    for i in range(0, 3):
        leo.left(120)
        leo.forward(side_length)
    leo.end_fill()

def mini_project():
    """Mini Project: """
    
    side_length: int = 100

    # create an initial triangle
    triangle_fill(side_length)
    
    # initialize bob
    bob: Turtle = Turtle()
    bob.speed(200)
    bob.pencolor("black")
    
    # move bob to starting point of leo
    bob.penup()
    bob.goto(45,60)
    bob.pendown()
    
    # outline leo's triangle
    for i in range(0, 3):
        bob.left(120)
        bob.forward(side_length)
    
    # Next utlines
    for i in range(0, 33):
        side_length = side_length * 0.95
        bob.left(121)
        bob.forward(side_length)
    
mini_project()
done()