def powers_of_numbers(x,y) :
    """Return the x to the power of y."""
    return (x ** y)

def root(x,y) :
    """Return the root of x to y"""
    return (x ** (1/y))
    
def add(x, y):
    """Return the sum of x and y."""
    return round (x + y, 3)

def subtract(x, y):
    """Return the difference of x and y."""
    return round (x - y, 3)

def multiply(x, y):
    """Return the product of x and y."""
    return round (x * y, 3)

def divide(x, y):
    """Return the result of dividing x by y.
    
    Raises:
        ZeroDivisionError: If y is 0.
    """
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return round (x / y, 3)
