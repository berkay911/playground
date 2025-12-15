def mult(a,b):
    result = a * b
    return result

def mult_recursion(a,b):
    # Base case
    if b == 1:
        return a
    else:
        return a + mult_recursion(a, b - 1)
    #recursive case
    
def fact(n):
    if n == 1:  # base case  we know factorioal of 1 is 1
        return 1
    else:       # recursive case
        return n * fact(n - 1)
    
#print(fact(3))

def power(a,b):
    if b == 0:  # base case
        return 1
    else:       # recursive case
        return a * power(a, b - 1)
    
#print(power(2,0)) 

def fibonacci(n):
    if n == 0:  # base case
        return 0
    elif n == 1: # base case
        return 1
    else:       # recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)
    
#print(fibonacci(6))  # Output: 8

d = {0: 0, 1: 1}  # dictionary to store previously computed Fibonacci numbers
def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        result = fib_efficient(n - 1, d) + fib_efficient(n - 2, d)
        d[n] = result
        return result
    
print(fib_efficient(50, d))  # Output: 12586269025 and it computes quickly


# different topic

x = {}
x["Alice"] = 25

print(x.get("Bob"))
print(x.get("Alice"))