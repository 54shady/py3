#!/usr/bin/env python

import random

secretNumber = random.randint(1, 20)
print('Guess a number in [1, 20]')

# Ask the player to guess 6 times
for guessesToken in range(1, 7):
    print('Take a guess[%d].' % guessesToken)
    guess = int(input())

    if guess < secretNumber:
        print('> %d' % guess)
    elif guess > secretNumber:
        print('< %d' % guess)
    else:
        break

if guess == secretNumber:
    print('Good job :)')
else:
    print('Secret Number is ' + str(secretNumber))

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
