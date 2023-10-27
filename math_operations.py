def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference of x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the result of dividing x by y.
    
    Raises:
        ZeroDivisionError: If y is 0.
    """
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return x / y
