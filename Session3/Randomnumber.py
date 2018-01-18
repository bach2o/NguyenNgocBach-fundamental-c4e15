from random import randint
x=randint(0, 100)
#loop = True
while True: #while loop:
    y=int(input("Enter a number between 0 and 100 "))
    if y == x:
        print("Congratulation! You guessed the correct number")
        break # loop = False

    elif abs(x-y) <= 2:
        print("Ooh, that's really close")
    elif 2 < abs(x-y) <= 5:
        print("Close enough")
    elif 5 < abs(x-y) <= 20:
        print("Shorten the gap")
    elif 20 < abs(x-y) <= 50:
        print("Long way to go")
    else:
        print("Light years away")
