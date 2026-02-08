# Model output for task_353

## Model
- devstral-small-2:24b-cloud

## Original Code:

def remove_column(list1, n):
   for i in list1: 
    del i[n] 
   return list1

## Refactored Code:

```python
def remove_column(list1, n):
    """Remove the nth column from each row in the 2D list."""
    for row in list1:
        del row[n]
    return list1
```

- Preserved the exact function name and parameter names
- Added a docstring to explain the function's purpose
- Renamed the loop variable from `i` to `row` for clarity
- Maintained the original behavior of modifying the input list in-place
- Kept the return statement unchanged
- Did not add any new functionality or fix any potential issues
- Preserved the original indentation and structure
- Did not change the variable `n` or its usage
