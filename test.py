import turtle
import time
import random

print ("This program draws shapes based on the number you enter in a uniform pattern.")
num_str = input("Enter the side number of the shape you want to draw: ")
if num_str.isdigit():
    squares = int(num_str)

angle = 180 - 180*(squares-2)/squares

turtle.up

x = 0
y = 0
turtle.setpos(x,y)


numshapes = 8
for x in range(numshapes):
    turtle.color(random.random(),random.random(), random.random())
    x += 5
    y += 5
    turtle.forward(x)
    turtle.left(y)
    for i in range(squares):
        turtle.begin_fill() # Begin the fill process.
        turtle.down() # "Pen" down?
        for i in range(squares):  # For each edge of the shape
            turtle.forward(40) # Move forward 40 units
            turtle.left(angle) # Turn ready for the next edge
        turtle.up() # Pen up
        turtle.end_fill() # End fill.


time.sleep(11)
turtle.bye()
