# Model output for task_107

## Model
- devstral-small-2:24b-cloud

## Original Code:

def count_Hexadecimal(L,R) :  
    count = 0;  
    for i in range(L,R + 1) : 
        if (i >= 10 and i <= 15) : 
            count += 1;  
        elif (i > 15) : 
            k = i;  
            while (k != 0) :  
                if (k % 16 >= 10) : 
                    count += 1;  
                k = k // 16;  
    return count;  

## Refactored Code:

```python
def count_Hexadecimal(L, R):
    count = 0
    for i in range(L, R + 1):
        if 10 <= i <= 15:
            count += 1
        elif i > 15:
            k = i
            while k != 0:
                if k % 16 >= 10:
                    count += 1
                k = k // 16
    return count
```

- Removed unnecessary semicolons for better readability
- Improved spacing around operators and after commas
- Simplified the range check condition from `if (i >= 10 and i <= 15)` to `if 10 <= i <= 15`
- Maintained all original logic and variable names exactly as in the input
- Preserved the exact same behavior as validated by the tests
- Kept the same indentation style (4 spaces)
- No changes to function signature or return values
- All conditional expressions remain unchanged in their logic
- The while loop structure and operations are identical to the original
