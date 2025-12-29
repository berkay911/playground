epsilon = 0.01
k = 25
guess = k / 2.0
num_guesses = 0

while abs(guess * guess - k) >= epsilon:
    num_guesses += 1
    guess = guess - (((guess ** 2) - k) / (2 * guess))

print('num_guesses = ' + str(num_guesses))
print('Square root of ' + str(k) + ' is about ' + str(guess))