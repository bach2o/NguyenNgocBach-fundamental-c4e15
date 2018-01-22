print('''
Hi there,
Think about a number from 0 to 100, then press Enter
''')
# Binarysearch

lo = 0
hi = 100
loop = True
while loop:
    mid = (lo + hi) // 2
    answer = input("Is {0} your number? ".format(mid))
    if answer.lower() == 'c':
        print("I knew it")
        loop = False
    elif answer.lower() == 's':
        hi = mid
    elif answer.lower() == 'l':
        lo = mid
    if lo == hi:
        print("You are cheating, aren't you?")
        break
