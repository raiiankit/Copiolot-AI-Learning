"""
calculator.py

A simple calculator module supporting basic arithmetic operations:
- add
- subtract
- multiply
- divide
"""

def add(a: float, b: float) -> float:
    """Return the sum of a and b"""
    return a + b

def subtract(a: float, b: float) -> float:
    """Return the difference of a and b"""
    return a - b

def multiply(a: float, b: float) -> float:
    """Return the product of a and b"""
    return a * b

def divide(a: float, b: float) -> float:
    """
    Return the division of a by b
    Raises ZeroDivisionError if b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b
