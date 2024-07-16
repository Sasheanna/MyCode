
# Draws a shape using "def" to decide the number of sides and the size using turtle.

import turtle
import random


randomColor = ('blue', 'purple', 'black', 'green', 'brown', 'red', 'pink', 'orange')

def polygon(sides, size, color):

    angle = 360/sides
    
    turtle.pendown()

    turtle.color(color)
    
    for a in range(sides):
        turtle.forward(size)
        turtle.right(angle)


# challenge:

""" hexagon made of 6 smaller hexagons

for b in range(6):
    
    polygon(6, 100, random.sample(randomColor,1))

    turtle.right(60)
"""


for c in range(8):

    turtle.penup()
    turtle.goto(100,100)

    polygon(12, 20, random.sample(randomColor,1))

    turtle.right(45)
