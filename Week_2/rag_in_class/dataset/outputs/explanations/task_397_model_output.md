# Model output for task_397

## Model
- devstral-small-2:24b-cloud

## Original Code:

def median_numbers(a,b,c):
 if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
 else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c
 return median

## Refactored Code:

```python
def median_numbers(a, b, c):
    if a > b:
        if a < c:
            median = a
        elif b > c:
            median = b
        else:
            median = c
    else:
        if a > c:
            median = a
        elif b < c:
            median = b
        else:
            median = c
    return median
```

- Maintained the exact same logic and structure of the original function
- Preserved all variable names and function signature
- Improved readability by consistent indentation and spacing
- Kept the nested if-elif-else structure intact
- Ensured all comparison operations remain unchanged
- Maintained the same return statement
- No changes to the conditional logic flow
- Preserved the original behavior as validated by tests
- Kept the same variable naming (median, a, b, c)
- No additional comments or docstrings added to avoid any interpretation changes
