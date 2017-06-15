import random

print('-------------------------------')
print('      NUMBER GUESS GAME')
print('-------------------------------')
print()

name = input('What is your name? ')
print()
the_number = random.randint(0,100)
guess = -1

while guess != the_number:
    guess = int(input('Guess a number between 0 and 100: '))

    if guess < the_number:
        print('Sorry {}, your guess of {} is too LOW'.format(name, guess))
        print()
    elif guess > the_number:
        print('Sorry {}, your guess of {} is too HIGH'.format(name, guess))
        print()
    else:
        print()
        print('{} is correct. You WIN {}!!'.format(guess, name))
