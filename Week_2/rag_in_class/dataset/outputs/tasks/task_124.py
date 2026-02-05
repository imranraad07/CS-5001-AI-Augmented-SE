import cmath

def angle_complex(a, b):
    """Calculate the phase angle of the complex number formed by a and b.

    Args:
        a: Real part of the complex number.
        b: Imaginary part of the complex number.

    Returns:
        The phase angle of the complex number in radians.
    """
    complex_number = complex(a, b)
    angle = cmath.phase(complex_number)
    return angle
