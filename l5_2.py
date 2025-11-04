increment = 0.01
epsilon = 0.1
guess = 0.0
x = 15

while (guess**2) < x+10:
    guess += increment
    if abs(guess**2 - x) < epsilon:
        print("The square root of", x, "is approximately", guess)
        break
    else:
        pass
