Diction = {
    "ng":"người, một loài linh trưởng bậc cao phát triển nhất trên Trái Đất",
    "ch":"chó, một loài động vật có vú thông minh, biết nghe lời chủ, thường được dùng trong nhiều món ăn của dân tộc Việt",
    "ny":"New York, thành phố giàu nhất hành tinh",
    "cc":"Con c*c, một loài động vật chưa xác định, cần sự tham gia khám phá của các nhà khoa học",
    "đmm": "Câu chửi thân thương của người Việt, do người Việt và vì người Việt"
}

# for x in Diction:
#     print(x, end=' ')
# print()
loop = True
while loop:
    print (*Diction)
    x = input('Nhập từ cần tra: ')
    if x in Diction:
        print(x, Diction[x])
    elif x == 'Thoát':
        break
    else:
        print('Không có từ cần tra')
        y = input('Bạn có muốn thêm từ này vào từ điển không? (Y / N)').upper()
        if y == 'Y':
            newmeaning = input('Nhập ý nghĩa')
            Diction[x] = newmeaning
    print('*'* 30)
