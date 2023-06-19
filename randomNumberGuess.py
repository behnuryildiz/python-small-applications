import random

randomNumber = random.randint(0, 50)
guess = int(input("Guess what a number it is till 50: \t"))
if guess > 50:
    print("Ups! Give a valid number!")

while True:
    guess = int(input("Give another try: \t"))
    if guess > 50:
        print("Ups! Give a valid number!")
    if guess == randomNumber:
        print("Right there! Congrats!")
        quit()
    elif guess in range (0, randomNumber-10):
        print("Your guess is too low.")

    elif guess in range (randomNumber+10, 51):
        print("That is too high.")

    elif guess in range (randomNumber-5, randomNumber+5):
        print("that is rarely near")