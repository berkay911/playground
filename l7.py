def sum(a, b):
    return a + b

def mult(a, b):
    return a * b

def calc(op, a, b):
    return op(a, b)

print(calc(sum, 2, 3))  # Output: 5