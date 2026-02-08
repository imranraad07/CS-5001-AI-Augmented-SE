# Model output for task_681

## Model
- devstral-small-2:24b-cloud

## Original Code:

def smallest_Divisor(n): 
    if (n % 2 == 0): 
        return 2; 
    i = 3;  
    while (i*i <= n): 
        if (n % i == 0): 
            return i; 
        i += 2; 
    return n; 

## Refactored Code:

```python
def smallest_Divisor(n):
    if n % 2 == 0:
        return 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
    return n
```

- Removed unnecessary parentheses around conditions
- Added consistent spacing around operators and after colons
- Maintained all original logic and variable names exactly
- Preserved the same indentation style (4 spaces)
- Kept the same return behavior for all cases
- No changes to the algorithm or control flow
- All test cases should pass without modification
