# Model output for task_488

## Model
- devstral-small-2:24b-cloud

## Original Code:

import math
def area_pentagon(a):
  area=(math.sqrt(5*(5+2*math.sqrt(5)))*pow(a,2))/4.0
  return area

## Refactored Code:

```python
import math

def area_pentagon(side_length):
    """Calculate the area of a regular pentagon given its side length.

    Args:
        side_length: Length of one side of the pentagon.

    Returns:
        The area of the pentagon.
    """
    constant = math.sqrt(5 * (5 + 2 * math.sqrt(5))) / 4.0
    return constant * (side_length ** 2)
```

- Renamed parameter from `a` to `side_length` for clarity
- Extracted the mathematical constant into a separate variable for better readability
- Replaced `pow(a, 2)` with `side_length ** 2` for Pythonic style
- Added docstring to explain the function's purpose, parameters, and return value
- Maintained the exact same mathematical formula and behavior
- Kept the same import statement for math module
- Preserved the function name `area_pentagon` to maintain API compatibility
- Improved code structure while keeping the same calculation logic
