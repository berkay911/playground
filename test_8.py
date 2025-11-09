cube = 27
epsilon = 0.01 
low = 0
high = cube
guess = (high + low) / 2.0
num_guesses = 0

while abs(guess**3 - cube) >= epsilon:
    if guess**3 > cube:
        high = guess
    else:
        low = guess
    guess = (high + low) / 2.0
    num_guesses += 1

print(f"Cube root of {cube} is about {guess}")
print(f"num_guesses = {num_guesses}")