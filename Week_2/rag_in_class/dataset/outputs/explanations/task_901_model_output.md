# Model output for task_901

## Model
- devstral-small-2:24b-cloud

## Original Code:

def smallest_multiple(n):
    if (n<=2):
      return n
    i = n * 2
    factors = [number  for number in range(n, 1, -1) if number * 2 > n]
    while True:
        for a in factors:
            if i % a != 0:
                i += n
                break
            if (a == factors[-1] and i % a == 0):
                return i

## Refactored Code:

```python
def smallest_multiple(n):
    if n <= 2:
        return n

    i = n * 2
    factors = [number for number in range(n, 1, -1) if number * 2 > n]

    while True:
        divisible = True
        for a in factors:
            if i % a != 0:
                i += n
                divisible = False
                break
        if divisible:
            return i
```

- Improved variable naming for clarity (e.g., `divisible` instead of implicit logic)
- Simplified the loop condition by separating the divisibility check
- Maintained the same logic flow and behavior as the original
- Kept the same input/output behavior validated by tests
- Reduced nesting levels for better readability
- Preserved the exact same algorithm and edge case handling
- Used consistent indentation and spacing
- Maintained the same performance characteristics
- Kept the same return value conditions
