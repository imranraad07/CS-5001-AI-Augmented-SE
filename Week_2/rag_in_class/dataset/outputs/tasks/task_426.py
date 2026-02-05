def filter_odd_numbers(numbers):
    """Return a list of odd numbers from the input list.

    Args:
        numbers: List of integers to filter.

    Returns:
        List of odd integers from the input.
    """
    return [num for num in numbers if num % 2 != 0]
