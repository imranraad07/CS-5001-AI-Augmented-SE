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

- Renamed loop variable `i` to more descriptive `row` to clarify it represents a row in the 2D list
- Added docstring to explain the function's purpose
- Maintained all original functionality including variable names and behavior
- Kept the same return statement and structure
- Preserved the exact same parameter names and types
- No changes to the core logic or operations performed
