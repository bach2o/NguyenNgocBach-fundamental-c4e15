menu=[]
stuffcount = 0
while stuffcount < 10:
    print("Hi there, here are your favorite things so far")
    print(*menu, sep=", ")
    print("Name one thing you want to add?")
    menu.append(input())
    print(*menu, sep=", ")
    count += 1
