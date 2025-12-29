class ElectronicDevice(object):
    def __init__(self, brand, model, power_status=False):
        self.brand = brand
        self.model = model
        self.power_status = power_status

    def power_on(self):
        self.power_status = True
        print(f"{self.brand} {self.model} is now ON.")
    def power_off(self):
        self.power_status = False
        print(f"{self.brand} {self.model} is now OFF.")
    
    def __str__(self):
        return f"{self.brand} {self.model} is {self.power_status}."
    

class Calculator(ElectronicDevice):
    #def __init__(self, brand, model, power_status=False):
    #    super().__init__(brand, model, power_status)

    def add(self, a, b):
        if self.power_status != True:
            return "Please turn on the calculator first."
        else:
            return a + b
        
    def subtract(self, a, b):   
        if self.power_status != True:
            return "Please turn on the calculator first."
        else:
            return a - b    
    def multiply(self, a, b):
        if self.power_status != True:
            return "Please turn on the calculator first."
        else:
            return a * b
    def divide(self, a, b):
        if self.power_status != True:
            return "Please turn on the calculator first."
        else:
            if b == 0:
                return "Error: Division by zero."
            return a / b
        

class Listoscope(ElectronicDevice):
    def __init__(self, brand, model, power_status=False, color = "black"):
        super().__init__(brand, model, power_status)
        self.color = color

    def measure_length(self, list_input):
        return len(list_input)
    
    def __str__(self):
        return f"{self.brand} {self.model} is {self.power_status}. Color: {self.color}."




class Fraction(object):
    """A simple Fraction class to represent fractions and perform basic operations."""
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        assert self.denominator != 0, "Denominator cannot be zero."

    def __doc__(self):
        return "I am a cooler fraction string"

    def __float__(self):
        return self.numerator / self.denominator
    
    def get_float_value(self):
        return self.numerator / self.denominator

    def add_fraction_to(self, other):
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __add__(self, other):
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)
    
    def __str__(self):
        if self.numerator != 0:
            return f"{self.numerator}/{self.denominator}"
        else:
            return f"{self.numerator}/{self.denominator}"