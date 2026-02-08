import cmath

def len_complex(a, b):
    """Calculate the magnitude (length) of a complex number formed by a and b."""
    complex_number = complex(a, b)
    magnitude = abs(complex_number)
    return magnitude
