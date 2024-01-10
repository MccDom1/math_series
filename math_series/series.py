# series.py

def fibonacci(n):
    """Return the nth value in the Fibonacci series."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def lucas(n):
    """Return the nth value in the Lucas numbers series."""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        a, b = 2, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def sum_series(n, a=0, b=1):
    """
    Return the nth value in a series defined by the initial values a and b.

    If a and b are not provided, the function defaults to the Fibonacci series.
    If a=2 and b=1, the function produces values from the Lucas numbers series.
    """
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
