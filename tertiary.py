# author: Samaiya Howard
# date: 7/23/2021

# --------------- # Section 3 # --------------- #
# ---------- # Part 1 # ---------- #

print('----- Section 3 -----'.center(25))
print('--- Part 1 ---'.center(25))

# Guessing Game - Warm Cold
#
# This is a spin on the number guessing game where the user must guess the correct number between 1 and 100. The
#   unknown number is random. The twist --> Instead of saying 'Too High' or 'Too Low', instead you will tell the user
#   if they are getting 'Warmer' or 'Colder'
#
# A user is getting 'Warmer' if the guess they just made has less of a difference than the previous guess.
# A user is getting 'Colder' if the guess they just made has a greater difference than the previous guess.
# On the first guess, simply inform the user if they are incorrect or correct.
#
# The user should have 10 tries to guess the number.
#
# HINT: You will not only need to keep track of the user's current guess, but also the last guess they made.
#   BE SURE TO UPDATE THE PREVIOUS GUESS TO THE NEW ONE AT SOME POINT IN THE LOOP, probably after you've determined
#   and informed the user if they are warmer or colder.
#
# WRITE CODE BELOW #
from random import randint #get the random number imported.
random_num = randint(1,100) #setting the random number between 1 and 100

print(random_num)
print('This guessing game is between 1-100!')
last_guess = None

for i in range(10):
    print('you have', 10 - i, 'guessed left.')
    guess = int(input("Enter a number: "))

    if i == 0:
        if guess != random_num:
            print('Your wrong')
        else:
            print('Correct!')
            break

    else:
        if guess == random_num:
            print('Correct! You guess the correct number! You have', 10 - i, 'guesses left! You did it in',i, 'guesses!')
            break
        elif abs(guess - random_num) < abs(last_guess - random_num):
            print('Warmer')
        elif abs(guess - random_num) > abs(last_guess - random_num):
            print('Colder')
        elif abs(guess - random_num) == abs(last_guess - random_num):
            print('No change')


    
    last_guess = guess 

if guess != random_num:
    print('Game over you guessed the number incorrectly the number was:', random_num)

# Getting Warmer --> The difference between the current guess and the secret is LESS THAN
#                       the difference between the last guess and the secret.

# Getting Colder --> The difference between the current guess and the secret is GREATER THAN
#                       the difference between the last guess and the secret.

# ---------- # Part 2 # ---------- #
print('\n' + ('--- Part 2 ---'.center(25)) + '\n')
# Calculate the Hamming Distance between two DNA strands.
#
# Your body is made up of cells that contain DNA. Those cells regularly wear out and need replacing, which they
#   achieve by dividing into daughter cells. In fact, the average human body experiences about 10 quadrillion
#   cell divisions in a lifetime!
#
# When cells divide, their DNA replicates too. Sometimes during this process mistakes happen and single pieces of
#   DNA get encoded with the incorrect information. If we compare two strands of DNA and count the differences
#   between them we can see how many mistakes occurred. This is known as the "Hamming Distance".
#
# We read DNA using the letters C,A,G and T. Two strands might look like this:
#
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
# ^ ^ ^  ^ ^    ^^
#
# They have 7 differences, and therefore the Hamming Distance is 7.
#
# The Hamming Distance is useful for lots of things in science, not just biology, so it's a nice phrase to
#   be familiar with :)
#
# Instructions
#   1. Prompt input from the user in the form of a DNA strand (as a String) and save it to a variable.
#       Do this twice.
#
#   2. Define a function called hamming() which accepts two parameters:
#       dna_strand1 | string | The first dna strand.
#       dna_strand1 | string | The second dna strand.
#
#       a. Using a loop inside the function, compare the two DNA strands to calculate the hamming distance.
#       b. Return the distance and print it out to the user.
#
#   HINT: It may be helpful to keep track of the distance using a variable. Think about what value it should have at
#       the beginning.
#
# WRITE CODE BELOW #
dna_input = input('enter a DNA sequence: ')
dna = input('enter a DNA sequence: ')


def hamming(dna_input, dna):
    difference = 0
    for i in range(len(dna)):
        if dna_input[i] != dna[i]:
            difference += 1
        
    print('hamming distance =',difference)
hamming(dna_input, dna)
