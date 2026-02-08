# Model output for task_101

## Model
- devstral-small-2:24b-cloud

## Original Code:

def kth_element(arr, n, k):
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] == arr[j+1], arr[j]
  return arr[k-1]

## Refactored Code:

```python
def kth_element(arr, n, k):
    # Perform bubble sort on the array
    for i in range(n):
        for j in range(0, n - i - 1):
            # Swap elements if they are in the wrong order
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] == arr[j + 1], arr[j]
    # Return the k-th smallest element (1-based index)
    return arr[k - 1]
```

- Preserved the exact function signature and variable names
- Added comments to explain the bubble sort algorithm and the purpose of the return statement
- Maintained the original logic including the bug in the swap operation (using `==` instead of `=`)
- Kept the same indentation and structure
- Did not modify the behavior in any way
- Preserved all unused variables and branches
- Maintained the same return value calculation
