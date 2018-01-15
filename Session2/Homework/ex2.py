import math
n=int(input("Please enter a positive integer"))
while True:
    if n >=0:
        ans = math.factorial(n)
        print(ans)
        break
    else:
        n=int(input("Please enter a positive integer"))
