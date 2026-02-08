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
    res = []
    res.append(0)
    res.append(1)
    i = 2
    while i < n + 1:
        res.append(max(i, (res[int(i / 2)]
                          + res[int(i / 3)]
                          + res[int(i / 4)]
                          + res[int(i / 5)])))
        i += 1
    return res[n]
```

- Maintained all original function names, variable names, and logic exactly as provided
- Improved readability by using consistent indentation and spacing
- Kept the same list initialization and append operations
- Preserved the exact same while loop condition and increment logic
- Maintained the same max calculation with identical integer division operations
- Kept the same return statement structure
- Did not introduce any new functionality or fix any potential bugs
- Preserved all original behavior as validated by the test suite
