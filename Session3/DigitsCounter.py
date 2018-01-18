#count=0
#while count <10:
#    x=int(input("Enter any number you want"))
#    print(len(str(abs(x))))
#    count += 1


digit = 0
x=abs(int(input("Enter any number you want ")))
while x > 0: #Bai cu la x >= 1
    x = x // 10 # n //=10 for short
    #Bai cu la x /10, tuy nhien nen lay phep chia lay phan nguyen //
    digit += 1
print(digit)
