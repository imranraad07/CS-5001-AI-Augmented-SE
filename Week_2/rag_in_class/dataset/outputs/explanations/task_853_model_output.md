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
    # Remove all factors of 2
    while n % 2 == 0:
        n = n // 2

    # Check for odd factors from 3 to sqrt(n)
    for i in range(3, int(math.sqrt(n) + 1)):
        count = 0
        curr_sum = 1
        curr_term = 1
        # While i divides n, process the factor
        while n % i == 0:
            count += 1
            n = n // i
            curr_term *= i
            curr_sum += curr_term
        res *= curr_sum

    # If remaining n is a prime > 2
    if n >= 2:
        res *= (1 + n)

    return res
```

- Maintained all original function names, variable names, and logic exactly as provided
- Added clear comments to explain the purpose of each code block
- Preserved all original indentation and structure
- Kept all original variable initializations and assignments
- Maintained the exact same control flow and loop structures
- Preserved the original behavior including the edge case handling for n >= 2
- Did not modify any mathematical operations or comparisons
- Kept all original return statements and their conditions
- Preserved all unused variables and their original usage patterns
