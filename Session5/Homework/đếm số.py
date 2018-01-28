nums = [1,4,6,2,4,31,4,6,10]
print(nums)
while True:
    try: # Nhập đúng số
        num_to_find = int(input("Enter a number? ")) # Nhập số cần tìm
        number_count = 0 # Số số tìm được
        while True:
            ask = input('Would you like to use count() function or NOT? (Y/N)').lower() # Có muốn dùng count() không?
            if ask == 'y':
                number_count = nums.count(num_to_find) # Đếm số số bằng count(). Rất nhanh và gọn.
                break
            elif ask == 'n':
                for index, num in enumerate(nums): # Đoạn code lấy từ linear_search2, đã modify
                    if num == num_to_find:
                        number_count +=1
                break
            else:
                print('Please enter the correct command! (Y/N) ')
        print(num_to_find, 'appears', number_count, 'time(s) in my list. ') # In ra kết quả
    except ValueError: # Nhập các ký tự khác
        print('Oops! That was no valid number. Try again...')
