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
def find_Max_Len_Even(str):
    n = len(str)
    i = 0
    currlen = 0
    maxlen = 0
    st = -1

    while i < n:
        if str[i] == ' ':
            if currlen % 2 == 0:
                if maxlen < currlen:
                    maxlen = currlen
                    st = i - currlen
            currlen = 0
        else:
            currlen += 1
        i += 1

    if currlen % 2 == 0:
        if maxlen < currlen:
            maxlen = currlen
            st = i - currlen

    if st == -1:
        return "-1"
    return str[st: st + maxlen]
```

- Maintained all original function names, variable names, and logic exactly as provided
- Improved code formatting with consistent indentation and spacing
- Removed unnecessary parentheses around conditions in while and if statements
- Kept all original variable initializations and assignments unchanged
- Preserved the exact same return logic and conditions
- Did not introduce any new functionality or fix any potential bugs
- Maintained the same control flow structure throughout the function
- Kept all original comments (none existed) and documentation unchanged
- Ensured the function signature remains identical to the original
- Preserved all edge case handling exactly as in the original implementation
