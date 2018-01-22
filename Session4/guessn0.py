print("Guess your number game!")
print("Now think of a number from 0 to 100, type it here and press 'Enter'. ")
print("All you have to do is to answer to my guess.")
print("'c' if my guess is 'C'orrect")
print("'s' if my guess is 'S'maller than your number")
print("'l' is my guess is 'L'arger than your number")
a=0
b=100
p = 0
d = 4
e = 9
count = 0
from random import randint
x = randint(a, b)
#while count < 10:
while True:
    print("Is",x,"your number?")
    Answer=input()
    if Answer == 'c':
        if count == p:
            print("I was reading your mind")
        elif p < count <= d:
            print("That was fast, wasn't it?")
        elif d < count <= e:
            print("I knew it! Took me a while though")
        else:
            print("Fucking finally")
        break
    elif Answer == 's':
        a = x + 1
        x = randint(a, b)
        count += 1
    elif Answer == 'l':
        b = x - 1
        x = randint(a, b)
        count +=1
    else:
        print('Huh? "c", "s", or "l" are valid responses.')

#Con mot truong hop nua do la minh choi ban?, so minh doan khong phai la so minh doan :)). Chua co cach lam.
