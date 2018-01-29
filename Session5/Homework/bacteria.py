# import math
while True:
    starting_bacteria = int(input('How many B bacterias are there? '))
    if starting_bacteria >= 0:
        time = int(input('How much time in minutes will we wait? '))
        if time >=0:
        # result = starting_bacteria*2**math.floor(time/2)
            result = starting_bacteria << (time // 2)
            print('After', time, 'minute(s) we would have', result, 'B bacterias')
            continue
        else:
            print('Please enter the appropriate value! ')
    else:
        print('Please enter the appropriate value! ')
