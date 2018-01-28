# 1. Tạo ra một list (int)
# 2. Hỏi người dùng nhập vào một số
# 3. Nói cho người dùng biết số này có tồn tại trong dãy không? Nếu có thì index
# là bao nhiêu?
nbrlist = [1,3,6,8,10]
guess = int(input('Enter a number >= {0} and <= {1}: '.format(min(nbrlist),max(nbrlist))))
# print(nbrlist.index(guess))
# answer = False
# for n in nbrlist:
#     if guess == n:
#         answer = True
#         print('Found', guess, 'in index', nbrlist.index(guess))
if guess in nbrlist:
    print('Found')
    pos = nbrlist.index(guess)
    print(pos)
else:
    print("Not found")
