count = 0
while count < 5:
    yob = int(input("Your year of birth? "))
    age = 2018 - yob

    if age < 10:
        print("Baby")
    elif age <18:
        print("Teenager")
    else:
        print("Adult")
    count += 1
#CtrlC +Enter to inturupt loop
# Dieu kien ban dau la count=5, dieu kien de vong lap con chay la count < 5, dieu kien thay doi la count +=1
# break chi tac dung len vong lap gan nhat
# vong for thi biet truoc so vong lap, con vong while thi chua biet truoc so vong lap
