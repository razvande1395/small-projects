import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

true_value = random.randint(0, 100)
difficulty = input("Choose your difficulty. Type 'easy' or 'hard'. ")

if difficulty == "easy":
    no_of_attempts = 10
else:
    no_of_attempts = 5

guessed_number = False

while True and no_of_attempts > 0:
    
    user_guess = int(input("Try to guess the number: "))

    if user_guess == true_value:
        print("Congratulations, you've guessed the number!")
        guessed_number = True
        break
        
    elif user_guess > true_value:
        print(f"Too high. Try again. {no_of_attempts - 1} attempts left.")
    else:
        print(f"Too low. Try again. {no_of_attempts - 1} attempts left.")

    no_of_attempts -= 1
    
if no_of_attempts == 0 and not guessed_number:
    print(f"You've exhausted all of your attempts and lost the game. The number was {true_value}.\nBetter luck next time!")