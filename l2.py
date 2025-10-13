#x = input("Write a verb pls: ")

#print(f"I can {x} better than you.")

import random

random_number = random.randint(-10,10)
user_guess = int(input("Guess a number between -100 and 100: "))

print(random_number==user_guess)
print(f"It was {random_number}")
