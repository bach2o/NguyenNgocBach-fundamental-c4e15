import random

#Variables
Wordlist = ('champion', 'meticulous', 'car', 'physics','anaconda','mouse')
word = random.choice(Wordlist)
correct = word
jumble = ''
guess = ''

while word:
    position = random.randrange(len(word))
    jumble += word[position] 
    word = word[:position] + word[(position + 1):]

print()
print(jumble)

guess = input('Your answer: ')
while guess != correct:
    print('Sorry, that\'s not the correct answer')
    guess = input('Your answer: ')

if guess == correct:
    print('Yay! Your answer is correct!')
    print()
    print('Thanks for playing!')

exit()
