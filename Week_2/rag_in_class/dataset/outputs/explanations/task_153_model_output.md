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
    y_coordinate = (4 * a * c - b * b) / (4 * a)
    vertex = (x_coordinate, y_coordinate)
    return vertex
```

- Extracted intermediate calculations into clearly named variables (`x_coordinate`, `y_coordinate`)
- Maintained the exact same mathematical operations and return structure
- Preserved all variable names and function signature as required
- Improved readability by breaking down the complex tuple assignment
- Kept the same order of operations to ensure identical behavior
- No changes to the logic or edge case handling
- Formatted for better visual clarity while keeping the same logic flow
