def sum (a, b):
    return a + b

def multiply (a, b):
    return a * b    

def analyze(a, b):
    my_tuple = (sum(a, b), multiply(a, b))
    return my_tuple
    

print(analyze(2, 3))
    