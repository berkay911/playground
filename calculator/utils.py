def sum(num1,num2):
    result = num1 + num2
    return result

def subtract(num1,num2):
    result = num1 - num2
    return result

def multiply(num1,num2):
    result = num1 * num2
    return result

def divide(num1,num2):
    if num2 == 0:
        return "Error: Division by zero"
    result = num1 / num2
    return result

def calculate_the_operation_i_choose(operation,num1,num2):
    return operation(num1,num2)
    
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
