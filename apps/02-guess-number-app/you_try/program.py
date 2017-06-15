import random

print('-------------------------------')
print('      NUMBER GUESS GAME')
print('-------------------------------')
print()

the_number = random.randint(0,100)
guess = -1

while guess != the_number:
    guess = int(input('Guess a number between 0 and 100: '))

    if guess < the_number:
        print('too low')
    elif guess > the_number:
        print('too high')
    else:
        print('You WIN!!')

print()
print('DONE...')