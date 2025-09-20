import random
guess_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Can you guess it?")

while True:
    guess = int(input("Enter your guess: "))

    if guess < guess_number:
        print("OOPS!! Too low! Try again.")
    elif guess > guess_number:
        print("OOPS!! Too High! Wrong guess, Try again")
    else:
        print(" Congratulations! You guessed it right.")
        break
