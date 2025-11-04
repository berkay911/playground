x = 54321
epsilon = 0.01
num_guesses = 0
low = 0.0
high = x
guess = (high + low) / 2

while abs(guess**2 - x) >= epsilon:
    print(f"low={low}, high={high}, guess={guess}")
    if guess**2 > x:
        high = guess
    else:
        low = guess
    guess = (high + low) / 2.0
    print("error=" + str(abs(guess**2 - x)))
    num_guesses += 1

if abs(guess**2 - x) >= epsilon:
    print(f"Failed on square root of {x}")
    print("last guess was " + str(guess))
    print("last guess squared was " + str(guess**2))
else:
    print(f"Square root of {x} is about {guess}")
print(f"num_guesses = {num_guesses}")