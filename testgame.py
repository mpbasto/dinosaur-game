# generate number 1~10
# input from user?
# check that input is a number 1~10
# check if number is the right guess
# otherwise ask again

import random
import sys

guessesTaken = 0
print('Greetings, stranger! What\'s your name?')
myName = input()

answer = random.randint(int(sys.argv[1]), int(sys.argv[2]))

print(f'Well, {myName}, I am thinking of a number between 1 and 10.')

while guessesTaken <= 3:
    print('Care to take a guess?')
    guess = int(input())
    guessesTaken = guessesTaken + 1
    try:
        if guess < answer:
            print('Ooof! That\'s too low!')
        elif guess > answer:
            print('Woah! That\'s too high!')
        elif guess == answer:
            break
    except ValueError:
        print('Woah woah woah! I just need a number.')
if guess == answer:
    guessesTaken = str(guessesTaken)
    print(
        f'Good job, {myName}! You guessed my number in {guessesTaken} guesses! 🥳🥳')
elif guess != answer:
    answer = str(answer)
    print(
        f'Nope! The number I was thinking of was {answer} 😕 \n Better luck next time!')
