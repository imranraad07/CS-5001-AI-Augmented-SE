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

- Consistent indentation and spacing for better readability
- Removed unnecessary parentheses in conditions
- Maintained all original variable names and function signature
- Preserved exact logic flow and behavior
- Kept the same return value format ("-1" for no match)
- No changes to the core algorithm or edge case handling
- All original comments (none) preserved
- Line length kept reasonable for readability
- No functional changes - only formatting improvements
