"""An exercise in remainders and boolean logic."""

#Sherin Stanley = "730404205"


# Begin your solution here...

num: int = int(input("Pick a number between 0-100: "))

if (num % 2 == 0 and num % 7 == 0):
    print("TAR HEELS")
elif (num % 7 == 0):
    print("HEELS")
elif (num % 2 == 0):
    print("TAR")
else: 
    print("CAROLINA")