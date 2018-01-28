times = 5
a, b  = 1, 1
month = 0

for x in range(times):
    print('Month ', month,':', b, ' pair(s) of rabbits')
    month += 1
    a, b = b, a + b
