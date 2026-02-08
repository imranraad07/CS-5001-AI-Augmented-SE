# Model output for task_453

## Model
- devstral-small-2:24b-cloud

## Original Code:

import math 
def sumofFactors(n) : 
    if (n % 2 != 0) : 
        return 0
    res = 1
    for i in range(2, (int)(math.sqrt(n)) + 1) :    
        count = 0
        curr_sum = 1
        curr_term = 1
        while (n % i == 0) : 
            count= count + 1
            n = n // i 
            if (i == 2 and count == 1) : 
                curr_sum = 0
            curr_term = curr_term * i 
            curr_sum = curr_sum + curr_term 
        res = res * curr_sum  
    if (n >= 2) : 
        res = res * (1 + n) 
    return res 

## Refactored Code:

```python
import math

def sumofFactors(n):
    if n % 2 != 0:
        return 0

    res = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        count = 0
        curr_sum = 1
        curr_term = 1

        while n % i == 0:
            count += 1
            n = n // i
            if i == 2 and count == 1:
                curr_sum = 0
            curr_term *= i
            curr_sum += curr_term

        res *= curr_sum

    if n >= 2:
        res *= (1 + n)

    return res
```

- Maintained all function names, variable names, and logic exactly as in the original
- Improved indentation and spacing for better readability
- Replaced compound operators (e.g., `count= count + 1`) with augmented assignment operators (e.g., `count += 1`)
- Kept the same mathematical operations and control flow
- Preserved all conditional checks and loop structures
- Maintained the same import statement
- Ensured the function signature remains unchanged
- Kept all comments (though there were none) and docstrings (though none existed) intact
- Verified that the behavior matches the original implementation exactly
