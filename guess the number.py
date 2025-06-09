import random

number = random.randint(1, 10)  # Corrected here
guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("Correct! You guessed it right.")
elif guess < number:
    print("Too low! Try again.")
else:
    print("Too high! Try again.")

print(f"The correct number was: {number}")
