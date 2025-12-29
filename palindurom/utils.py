def is_palindrome(input_string):
    """Check if the given string is a palindrome."""
    if input_string == input_string[::-1]:
        return True
    else:
        return False
    
def bisection_sqrt(x):
    """Approximate the square root of x using the bisection method."""
    
    epsilon = 0.01
    low = 0
    high = x
    guess = (low + high) / 2.0

    while abs(guess**2 - x) >= epsilon:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0

    return guess