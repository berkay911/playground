x = 16
guess = 0.0

while (guess**2) < x:
    guess += 1.0
if guess**2 == x:
    print('Square root of', x, 'is', guess)
else:
    print(x, 'is not a perfect square')