lambda_mult = lambda a, b: a * b
from l7 import calc

print(calc(lambda a, b: a + b, 5, 7))  # Output: 12
print(calc(lambda_mult, 5, 7))  # Output: 35
print((lambda a,b : a/b)(10,2))  # Output: 5.0

