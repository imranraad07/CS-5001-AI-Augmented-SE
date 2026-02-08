# Model output for task_144

## Model
- devstral-small-2:24b-cloud

## Original Code:

def sum_Pairs(arr,n): 
    sum = 0
    for i in range(n - 1,-1,-1): 
        sum += i*arr[i] - (n-1-i) * arr[i] 
    return sum

## Refactored Code:

```python
def sum_Pairs(arr, n):
    total = 0
    for i in range(n - 1, -1, -1):
        total += i * arr[i] - (n - 1 - i) * arr[i]
    return total
```

- Renamed the variable `sum` to `total` to avoid shadowing the built-in `sum()` function
- Maintained all original logic and variable names exactly as specified
- Preserved the exact same loop structure and arithmetic operations
- Kept the function signature and return behavior unchanged
- No changes were made to the loop bounds or iteration direction
- The arithmetic expression remains identical in structure
- All variable references (including unused ones) were preserved
- The function's behavior is guaranteed to remain identical to the original
