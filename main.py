import random


secret_number = random.randint(1, 100)
max_attempts = 7  # Maximum number of attempts allowed
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess the number.")

while attempts < max_attempts:
    # Ask the user to guess the number
    guess = int(input("Guess the number: "))
    attempts += 1
    
    # Check if the guess is correct
    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

# If the player runs out of attempts
if attempts == max_attempts:
    print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")
