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

def area_pentagon(a):
    """Calculate the area of a regular pentagon with side length a."""
    area = (math.sqrt(5 * (5 + 2 * math.sqrt(5))) * pow(a, 2)) / 4.0
    return area
```

- Preserved the exact mathematical formula for pentagon area calculation
- Added a docstring to explain the function's purpose
- Maintained all variable names and function signature exactly as in the original
- Kept the same import statement for the math module
- Ensured the calculation logic remains unchanged
- Formatted the code with consistent indentation and spacing
- Did not modify the return statement or its behavior
- Preserved the floating-point division (4.0) as in the original
