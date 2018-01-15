from turtle import *
speed(0)
n=int(3)

for i in range(4):
    for i in range(n):
        if n % 2 == 0:
            color('red')
        else:
            color('blue')
        forward(100)
        left(360/n)

    n=n+1
mainloop()
