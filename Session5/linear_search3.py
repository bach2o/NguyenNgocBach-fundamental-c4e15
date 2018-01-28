nums = [1,4,6,2,4,31,4,6,10]
num_to_find = int(input("Enter a number?"))

for index, num in enumerate(nums):
    if num == num_to_find:
        print('Found at index: ',index)
        break
else: # did not run into break
    print('Not found')
