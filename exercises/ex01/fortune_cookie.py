"""Program that outputs one of at least four random, good fortunes."""

#Sherin Stanley="730404205"
# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

print("Your fortune cookie says...")

how_much: int = int(input("Pick a number between 0-100: "))

if how_much < 50: 
    print("A beautiful, smart, and loving person will be coming intro your life. Now, go spread positive vibes!")
else:
    if how_much < 75:
        print("Your life will be happy and peaceful.")
    else:
        print("Soon life with become more interesting.")
print("Now, go spread positive vibes!")