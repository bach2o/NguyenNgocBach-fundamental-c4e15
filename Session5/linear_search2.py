nums = [1,4,6,2,4,31,4,6,10]
num_to_find = int(input("Enter a number?"))

# 1. Assumption / Gia dinh ve ket qua
found_index = [] #Not found
# 2. Create a loop to test our assumption
for index, num in enumerate(nums):
    if num == num_to_find:
        found_index.append(index) # Update Assumption

if found_index == []:
    print('Not found')
else:
    print('Found at index', found_index)
