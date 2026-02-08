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
- Removed semicolons at the end of statements
- Improved indentation consistency
- Maintained all original logic and variable names exactly
- Preserved the exact same behavior as the original implementation
- Kept the same function signature and return structure
- Did not introduce any new functionality or fix any potential bugs
- Ensured all test cases would pass without modification
