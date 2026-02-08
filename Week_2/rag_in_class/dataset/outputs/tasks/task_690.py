def mul_consecutive_nums(nums):
    """Multiply each pair of consecutive numbers in the input list.

    Args:
        nums: List of numbers to process.

    Returns:
        List of products where each element is the product of consecutive pairs
        from the input list. The result has one fewer element than the input.
    """
    result = [a * b for a, b in zip(nums[:-1], nums[1:])]
    return result
