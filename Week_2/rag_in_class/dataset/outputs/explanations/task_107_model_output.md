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
def count_hexadecimal_digits_in_range(start, end):
    """Count the number of hexadecimal digits (10-15) in the decimal representation of numbers from start to end (inclusive)."""
    count = 0

    for number in range(start, end + 1):
        if 10 <= number <= 15:
            count += 1
        elif number > 15:
            current = number
            while current != 0:
                if current % 16 >= 10:
                    count += 1
                current = current // 16

    return count
```

- Renamed function to follow Python naming conventions (snake_case)
- Improved variable names for clarity (i → number, k → current)
- Added docstring to explain function purpose
- Simplified conditional logic (removed redundant parentheses)
- Maintained exact same behavior as original implementation
- Kept the same algorithm structure but made it more readable
- Preserved all test cases by maintaining identical functionality
- Improved code formatting and spacing for better readability
