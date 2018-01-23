Clothes = ['T-Shirt', 'Sweater']
while True:
    Acts = input('Welcome to our shop, what do you want (C, R, U, D)?' ).upper()
    if Acts == 'R':
        print('Our items: ', end='')
        print(*Clothes, sep=', ')
    elif Acts == 'C':
        Clothes.append(input('Enter new item:'))
        print('Our items: ', end='')
        print(*Clothes, sep=', ')
    elif Acts == 'U':
        while True:
            i  = int(input('Update position?' ))
            if i > len(Clothes):
                print('Please enter the correct position.')
            else:
                Clothes[i - 1] = input('New item?')
                print('Our items: ', end='')
                print(*Clothes, sep=', ')
                break
    elif Acts == 'D':
        while True:
            i  = int(input('Delete position?' ))
            if i > len(Clothes):
                print('Please enter the correct position.')
            else:
                Clothes.pop(i - 1)
                print('Our items: ', end='')
                print(*Clothes, sep=', ')
                break
    else:
        print('Please enter the correct command!')
