# Model output for task_853

## Model
- devstral-small-2:24b-cloud

## Original Code:

import math
def sum_of_odd_Factors(n): 
    res = 1
    while n % 2 == 0: 
        n = n // 2 
    for i in range(3,int(math.sqrt(n) + 1)): 
        count = 0
        curr_sum = 1
        curr_term = 1
        while n % i == 0: 
            count+=1 
            n = n // i 
            curr_term *= i 
            curr_sum += curr_term    
        res *= curr_sum  
    if n >= 2: 
        res *= (1 + n) 
    return res 

## Refactored Code:

```python
import math

def sum_of_odd_Factors(n):
    res = 1
    # Remove all factors of 2 (even factors)
    while n % 2 == 0:
        n = n // 2

    # Check for odd factors starting from 3 up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1):
        count = 0
        curr_sum = 1  # Start with 1 to account for the factor itself
        curr_term = 1

        # Extract all occurrences of current factor i
        while n % i == 0:
            count += 1
            n = n // i
            curr_term *= i
            curr_sum += curr_term

        res *= curr_sum

    # If remaining n is a prime number >= 2, add it to the sum
    if n >= 2:
        res *= (1 + n)

    return res
```

- Maintained all function names, variable names, and logic exactly as in the original
- Added clear comments to explain each section of the code
- Preserved the original indentation and structure
- Kept the same mathematical operations and control flow
- Ensured the same edge case handling (n >= 2 check)
- Maintained the same initialization values (res = 1, curr_sum = 1, etc.)
- Kept the same loop conditions and termination criteria
- Preserved the exact same return statement
- Did not modify any variable names or function signatures
- Ensured the code would pass all existing tests without behavior changes
