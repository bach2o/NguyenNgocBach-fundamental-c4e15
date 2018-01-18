from getpass import getpass

count=0
while count<3:
    username=input("Username:")
    if username == "admin123":
        password=getpass("Password:")
        if password == "thedog":
            print("Welcome to the system, admin")
            break
        else:
            print("Password is incorrect.")
            count +=1
    elif username == "Fuckyou":
        print("Well good heaven! We've got a present for you, too! :D",'''
    ░░░░░░░░░░░░░░░▄▄░░░░░░░░░░░
    ░░░░░░░░░░░░░░█░░█░░░░░░░░░░
    ░░░░░░░░░░░░░░█░░█░░░░░░░░░░
    ░░░░░░░░░░░░░░█░░█░░░░░░░░░░
    ░░░░░░░░░░░░░░█░░█░░░░░░░░░░
    ██████▄███▄████░░███▄░░░░░░░
    ▓▓▓▓▓▓█░░░█░░░█░░█░░░███░░░░
    ▓▓▓▓▓▓█░░░█░░░█░░█░░░█░░█░░░
    ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░█░░░
    ▓▓▓▓▓▓█░░░░░░░░░░░░░░░░█░░░░
    ▓▓▓▓▓▓█░░░░░░░░░░░░░░██░░░░░
    ▓▓▓▓▓▓█████░░░░░░░░░██░░░░░░''')
        count +=1
    else:
        print("Username is incorrect")
        count +=1
