import random

random_number = random.randint(-10,10)
print(random_number)
user_guess = input("Guess a number between -10 and 10: ")


if type(user_guess) == int:
    if user_guess==random_number:
        print("You guessed it right.")

    elif user_guess>random_number:
        print("Your number is bigger.")

    elif user_guess<random_number:
        print("Your number is smaller.")

else:
    print("Invalid Input")
