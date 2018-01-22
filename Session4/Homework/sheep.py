size = [5, 7, 300, 90, 24, 50, 75]
print('Hello, my name is Bach and these are my sheep sizes')
print(size)
print()
highest = max(size)
print('Now my biggest sheep has size', highest , "let's shear it")
print()
print('After shearing, here is my flock')
size[size.index(highest)] = 8
print(size)
loop = True
month = 1
while loop:
    print('MONTH:',month)
    print('One month has passed, now here is my flock')
    for i, items in enumerate(size):
        size[i] = size[i] + 50
    print(size)
    highest = max(size)
    print('Now my biggest sheep has size', highest , "let's shear it")
    print('After shearing, here is my flock')
    size[size.index(highest)] = 8
    print(size)
    month +=1
    print()
    if month == 4:
        loop=False
total_size = sum(size)
print('My flock has size in total:', total_size)
print('I would get', total_size,'* 2$ =', total_size * 2,'$')
