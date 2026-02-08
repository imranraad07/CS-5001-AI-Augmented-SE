# Model output for task_315

## Model
- devstral-small-2:24b-cloud

## Original Code:

def find_Max_Len_Even(str): 
    n = len(str) 
    i = 0
    currlen = 0
    maxlen = 0
    st = -1
    while (i < n): 
        if (str[i] == ' '): 
            if (currlen % 2 == 0): 
                if (maxlen < currlen): 
                    maxlen = currlen 
                    st = i - currlen 
            currlen = 0 
        else : 
            currlen += 1
        i += 1
    if (currlen % 2 == 0): 
        if (maxlen < currlen): 
            maxlen = currlen 
            st = i - currlen 
    if (st == -1): 
        return "-1" 
    return str[st: st + maxlen] 

## Refactored Code:

```python
def find_max_len_even(s):
    """Return the longest even-length substring without spaces, or '-1' if none exists."""
    max_length = 0
    max_start = -1
    current_length = 0
    current_start = 0

    for i, char in enumerate(s):
        if char == ' ':
            if current_length % 2 == 0 and current_length > max_length:
                max_length = current_length
                max_start = current_start
            current_length = 0
            current_start = i + 1
        else:
            current_length += 1

    if current_length % 2 == 0 and current_length > max_length:
        max_length = current_length
        max_start = current_start

    return s[max_start:max_start + max_length] if max_start != -1 else "-1"
```

- Renamed function and variables to follow Python naming conventions (snake_case)
- Replaced while loop with for loop using enumerate for cleaner iteration
- Simplified logic by tracking current_start separately
- Removed redundant checks by combining conditions
- Improved readability with consistent spacing and comments
- Maintained exact same behavior as original implementation
- Added docstring to explain function purpose
- Reduced nesting levels for better readability
- Preserved all edge case handling (empty string, no valid substrings, etc.)
