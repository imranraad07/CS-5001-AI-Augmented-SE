# Model output for task_431

## Model
- devstral-small-2:24b-cloud

## Original Code:

def common_element(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result

## Refactored Code:

```python
def common_element(list1, list2):
    """Check if there is any common element between two lists.

    Args:
        list1: First list of elements.
        list2: Second list of elements.

    Returns:
        bool: True if there is at least one common element, False otherwise.
    """
    return any(x in list2 for x in list1)
```

- Replaced nested loops with a more Pythonic `any()` and generator expression
- Added docstring to explain the function's purpose, arguments, and return value
- Maintained the same behavior (returns True as soon as a common element is found)
- Improved readability by reducing nesting and using built-in functions
- Kept the same function signature and return type
- The refactored version is more efficient as it can short-circuit on the first match
- Removed unnecessary variable `result` and intermediate assignments
- The logic is now more concise while being equally clear
