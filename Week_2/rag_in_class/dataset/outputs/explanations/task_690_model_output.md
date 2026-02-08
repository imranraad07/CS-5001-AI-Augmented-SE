# Model output for task_690

## Model
- devstral-small-2:24b-cloud

## Original Code:

def mul_consecutive_nums(nums):
    result = [b*a for a, b in zip(nums[:-1], nums[1:])]
    return result

## Refactored Code:

```python
def mul_consecutive_nums(nums):
    """Multiply each pair of consecutive numbers in the input list.

    Args:
        nums: List of numbers to process.

    Returns:
        List of products where each element is the product of consecutive pairs
        from the input list (e.g., [a*b, b*c, c*d] for input [a, b, c, d]).
    """
    result = [b * a for a, b in zip(nums[:-1], nums[1:])]
    return result
```

- Preserved the exact function name and variable names
- Added a docstring to explain the function's purpose and behavior
- Maintained the original list comprehension logic without modification
- Kept the same return statement structure
- No changes to the core algorithm or behavior
- Formatting remains consistent with original (no unnecessary whitespace changes)
- All variable names (a, b, nums, result) remain unchanged
- The zip operation and slicing logic is identical to original
