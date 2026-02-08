# Model output for task_392

## Model
- devstral-small-2:24b-cloud

## Original Code:

def get_max_sum (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]

## Refactored Code:

```python
def get_max_sum(n):
    # Initialize the result list with base cases
    res = [0, 1]

    # Iterate from 2 to n (inclusive)
    for i in range(2, n + 1):
        # Calculate the maximum sum for current index
        current_max = max(
            i,
            res[i // 2] + res[i // 3] + res[i // 4] + res[i // 5]
        )
        res.append(current_max)

    return res[n]
```

- Replaced while loop with a more Pythonic for loop
- Improved variable naming (res -> current_max for clarity)
- Used integer division operator (//) instead of int() for better readability
- Maintained exact same logic and behavior
- Preserved all function and variable names as required
- Improved code formatting and indentation
- Kept the same return value structure
- Maintained the same list initialization pattern
- Preserved the exact same mathematical operations
