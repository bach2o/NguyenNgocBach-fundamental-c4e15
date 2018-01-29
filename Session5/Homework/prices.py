prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
total = 0
individual_cost = 0
for key in prices:
    print(key)
    print('price: ',prices[key])
    print('stock: ',stock[key])
    print()
for key in prices:
    individual_cost = prices[key]*stock[key]
    total = total + individual_cost
print('Total: ',total)
