# Model output for task_153

## Model
- devstral-small-2:24b-cloud

## Original Code:

def parabola_vertex(a, b, c): 
  vertex=(((-b / (2 * a)),(((4 * a * c) - (b * b)) / (4 * a))))
  return vertex

## Refactored Code:

```python
def parabola_vertex(a, b, c):
    x_coordinate = -b / (2 * a)
    y_coordinate = ((4 * a * c) - (b * b)) / (4 * a)
    vertex = (x_coordinate, y_coordinate)
    return vertex
```

- Maintained the exact same function signature and return behavior
- Split the complex tuple assignment into clear, separate variable assignments
- Used descriptive variable names for intermediate calculations
- Preserved all mathematical operations exactly as they were
- Kept the same return statement structure
- Did not modify any variable names or function names
- Maintained the same order of operations in calculations
- Preserved the original tuple packing for the return value
