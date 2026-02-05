def multiply_consecutive_numbers(numbers):
    """Return a list of products of each pair of consecutive numbers in the input list.

    Args:
        numbers: List of numbers to process

    Returns:
        List of products where each element is the product of consecutive pairs
        from the input list. The result has one fewer element than the input.
    """
    if len(numbers) < 2:
        return []

    return [a * b for a, b in zip(numbers[:-1], numbers[1:])]
