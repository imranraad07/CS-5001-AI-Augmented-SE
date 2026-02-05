def median_numbers(a, b, c):
    """Return the median of three numbers."""
    if (a <= b <= c) or (c <= b <= a):
        return b
    if (b <= a <= c) or (c <= a <= b):
        return a
    return c
