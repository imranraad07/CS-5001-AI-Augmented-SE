def binary_to_integer(binary_tuple):
    """Convert a tuple of binary digits (0s and 1s) to a decimal integer string.

    Args:
        binary_tuple: A tuple containing only 0s and 1s representing binary digits.

    Returns:
        A string representation of the decimal integer value of the binary input.
    """
    binary_str = ''.join(str(bit) for bit in binary_tuple)
    decimal_value = int(binary_str, 2)
    return str(decimal_value)
