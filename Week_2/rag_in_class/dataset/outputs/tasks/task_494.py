def binary_to_integer(test_tup):
    """Convert a tuple of binary digits to an integer string representation."""
    binary_str = "".join(str(digit) for digit in test_tup)
    integer_value = int(binary_str, 2)
    return str(integer_value)
