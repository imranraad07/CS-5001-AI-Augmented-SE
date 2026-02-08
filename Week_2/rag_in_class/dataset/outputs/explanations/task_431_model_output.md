# Model output for task_431

## Model
- devstral-small-2:24b-cloud

## Original Code:

def common_element(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result

## Refactored Code:

```python
def common_element(list1, list2):
    for x in list1:
        for y in list2:
            if x == y:
                return True
```

- Removed redundant initialization of `result` variable since it's always overwritten before use
- Simplified the logic by directly returning `True` when a match is found
- Maintained the exact same behavior including the early return on first match
- Preserved all function and variable names exactly as in the original
- Kept the nested loop structure unchanged
- Maintained the same return value types (boolean)
- Preserved the original function signature and scope
- Did not add any new functionality or fix any potential issues
