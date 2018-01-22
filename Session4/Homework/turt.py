from turtle import *
import turtle
speed(0)
n=int(3)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i, color in enumerate(colors):
    turtle.color(color)
    for i in range(n):
        forward(100)
        left(360/n)
    n=n+1
mainloop()
