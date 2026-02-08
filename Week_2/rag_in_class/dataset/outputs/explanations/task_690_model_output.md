# Model output for task_690

## Model
- devstral-small-2:24b-cloud

## Original Code:

def mul_consecutive_nums(nums):
    result = [b*a for a, b in zip(nums[:-1], nums[1:])]
    return result

## Refactored Code:

```python
def multiply_consecutive_numbers(numbers):
    """Multiply each pair of consecutive numbers in the input list.

    Args:
        numbers: List of numbers to process.

    Returns:
        List of products of consecutive pairs.
    """
    return [a * b for a, b in zip(numbers[:-1], numbers[1:])]
```

- Renamed function to be more descriptive (`mul_consecutive_nums` → `multiply_consecutive_numbers`)
- Renamed parameter to be more descriptive (`nums` → `numbers`)
- Added docstring explaining the function's purpose, arguments, and return value
- Maintained the same logic and behavior as the original implementation
- Kept the list comprehension for concise and readable iteration
- Preserved the exact same functionality validated by the tests
