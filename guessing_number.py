import random

number = random.randint(1, 100)
attempts = 0
max_attempts = 10

print(" WELCOME! YOU ARE GOING TO PLAY A NUMBER GUESSING GAME")
print("I'm thinking of a number between 1 and 100...")
print(f"You have only {max_attempts} attempts to guess it!\n")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print(f"  Too low! Attempts left: {max_attempts - attempts}\n")
    elif guess > number:
        print(f"  Too high! Attempts left: {max_attempts - attempts}\n")
    else:
        print(f" Woowww!! You guessed it right in {attempts} attempts 😎")
        break

if guess != number:
    print(f"\n  Game Over! The correct number was {number}")
