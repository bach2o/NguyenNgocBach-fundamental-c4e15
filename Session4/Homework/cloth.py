Clothes = ['T-Shirt', 'Sweater']
while True:
    Acts = input('Welcome to our shop, what do you want (C, R, U, D)?' ).upper()
    if Acts == 'R':
        print('Our items:', Clothes)
    elif Acts == 'C':
        Clothes.append(input('Enter new item:'))
        print('Our items:', Clothes)
    elif Acts == 'U':
        i  = int(input('Update position?' ))
        Clothes[i - 1] = input('New item?')
        print('Our items:', Clothes)
    elif Acts == 'D':
        i  = int(input('Delete position?' ))
        Clothes.pop(i - 1)
        print('Our items:', Clothes)
    else:
        print('Please enter the correct command!')
