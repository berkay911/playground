def divide(x, y):
    assert type(x) == int, "First argument must be an integer"
    assert type(y) == int, "Second argument must be an integer"
    



    try:
        return x / y
    except ZeroDivisionError:
        print("Denom is 0 so the answer is infinite")
        return float('inf')
    except TypeError:
        raise TypeError("Both arguments must be integers or floats")
    except:
        print("Something went wrong")
    finally:
        print("Execution completed")


print(divide(10, "a"))

