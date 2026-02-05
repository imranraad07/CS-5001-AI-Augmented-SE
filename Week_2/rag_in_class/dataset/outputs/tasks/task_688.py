import cmath

def len_complex(a: float, b: float) -> float:
    """Calculate the magnitude of a complex number given its real and imaginary parts.

    Args:
        a: The real part of the complex number.
        b: The imaginary part of the complex number.

    Returns:
        The magnitude (length) of the complex number.
    """
    complex_number = complex(a, b)
    return abs(complex_number)
