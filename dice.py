# dice rolling simulator
# import random module to a randomly selected element from the specified range
import random

print("Welcome to dice rolling simulator.")
print("Do you want to generate a random number between 1 and 6?")
# while loop to ask user if they want to play and retrieve a random number if they do
while True:
    input1 = input("y/n? ")  # repeating question while the loop is true
    input2 = input1.lower().strip()  # make sure there no extra spaxes and input is lower case
    if input2 == "y":  # if the input equals y output a random number between 1 and 6
        # print the random number, the range 1 and 7 as the last number is not printed
        print(random.randrange(1, 7))
    elif input2 == "n":  # if input equals to n quit
        break
    else:
        # if input is not y or n tell the user to enter y/n
        print("Please enter y to continue or n to quit.")
