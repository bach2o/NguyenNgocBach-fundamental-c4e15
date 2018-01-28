alphabet = 'abcdefghijklmnopqrstuvwxyz'
space = ' '
number = '12345667890'
character_table = {}
loop = True
while loop:
    x = input("Enter a sentence: ")
    x = x.lower()
    unidentified_char = 0
    if x == 'exit':
        loop = False
    else:
        for char in x:
            if char in alphabet: # chữ cái
                if char in character_table:
                    character_table[char] = character_table[char] + 1
                else:
                    character_table[char] = 1
            elif char in number: # số
                if char in character_table:
                    character_table[char] = character_table[char] + 1
                else:
                    character_table[char] = 1
            elif char in space: # dấu cách
                if char in character_table:
                    character_table[char] = character_table[char] + 1
                else:
                    character_table[char] = 1
            else:
                unidentified_char +=1 # các ký tự đặc biệt
        if x == '':
            print('Please enter the appropriate sentence. ')
        keys = character_table.keys()
        for char in sorted(keys):
            print(char, character_table[char])
        print('Unidentified Character(s) Found: ', unidentified_char)
        character_table = {}
