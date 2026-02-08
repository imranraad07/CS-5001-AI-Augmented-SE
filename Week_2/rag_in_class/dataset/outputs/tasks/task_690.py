def multiply_consecutive_numbers(numbers):
    """Multiply each pair of consecutive numbers in the input list.

    Args:
        numbers: List of numbers to process.

    Returns:
        List of products of consecutive pairs.
    """
    return [a * b for a, b in zip(numbers[:-1], numbers[1:])]
