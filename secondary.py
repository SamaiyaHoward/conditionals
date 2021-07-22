# author:
# date:

# --------------- # Section 2 # --------------- #
# ---------- # Part 1 # ---------- #

print('----- Section 2 -----'.center(25))
print('--- Part 1 ---'.center(25))

# 2 - Palindrome
print('\n' + 'Task 1' + '\n')
#
# Background: A palindrome is a word that is the same if read forwards and backwards. Examples of palindromes include:
#   - mom
#   - dad
#   - radar
#   - deified
#
# Instructions
#   a. Prompt input from the user in the form of a word.
#   b. Determine if the word is a palindrome.
#       a. If so, print that the word is a palindrome.
#       b. Otherwise, print that the word is not a palindrome.


# 2 - for Loop Patterns
print('\n' + 'Task 2' + '\n')
#
#
# Instructions
#   a. Create at least two of the following patterns using for loops and conditionals. One has been done for you as an
#       example. You still have to do two more. You are free to choose which ones you do.
#   b. Use the symbol specified by the user.

# $$$$$ | i = 0
# $     | i = 1
# $     | i = 2
# $$$$$ | i = 3
# $     | i = 4
# $     | i = 5
# $$$$$ | i = 6

# When i is evenly divisible by 3 --> 5 symbols. Otherwise, 1 symbol.

s = input('>> symbol | ')

for i in range(7):
    if i % 3 == 0:
        print(s * 5)
    else:
        print(s)

print()

# ****
# *   *
# *   *
# *   *
# *   *
# *   *
# ****


# &
# &
# &
# &
# &
# &&&&&


# @   @
# @   @
#  @ @
#   @
#  @ @
# @   @
# @   @


# -------
#      -
#     -
#    -
#   -
#  -
# -------
