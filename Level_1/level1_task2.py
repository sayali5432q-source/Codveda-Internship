import random

number = random.randint(1, 100)

max_attempts = 5

print("🎯 Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("You have", max_attempts, "attempts to guess it.")

for attempt in range(1, max_attempts + 1):

    guess = int(input("Enter your guess: "))

    if guess == number:
        print("🎉 Correct! You guessed the number!")
        print("You guessed it in", attempt, "attempt(s).")
        break

    elif guess < number:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")

else:
    print("😔 Game Over!")
print("The correct number was:", number)