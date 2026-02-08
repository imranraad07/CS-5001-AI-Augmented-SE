def even_bit_toggle_number(n):
    """Toggle all even-positioned bits (0-indexed) in the binary representation of n.

    Args:
        n: Integer to process

    Returns:
        Integer with even-positioned bits toggled
    """
    mask = 0
    position = 0

    while n > 0:
        if position % 2 == 1:
            mask |= 1 << position
        position += 1
        n >>= 1

    return n ^ mask
