import math

def area_pentagon(side_length):
    """Calculate the area of a regular pentagon given its side length.

    Args:
        side_length: Length of one side of the regular pentagon.

    Returns:
        The area of the pentagon.
    """
    constant = math.sqrt(5 * (5 + 2 * math.sqrt(5))) / 4.0
    return constant * (side_length ** 2)
