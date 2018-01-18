col=int(input("enter columns"))
row=int(input("enter rows"))
for y in range(row):
    for x in range(col):
        if ( x + y ) % 2 == 0:
            print("x",end="")
        else:
            print("*",end="")
    print()
