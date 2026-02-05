import cmath

def convert(numbers):
    """Convert a number or sequence of numbers to polar coordinates.

    Args:
        numbers: A number or sequence of numbers to convert.

    Returns:
        A tuple or sequence of tuples representing the polar coordinates
        (magnitude, phase) of the input numbers.
    """
    return cmath.polar(numbers)
