# Model output for task_395

## Model
- devstral-small-2:24b-cloud

## Original Code:

def first_non_repeating_character(str1):
  char_order = []
  ctr = {}
  for c in str1:
    if c in ctr:
      ctr[c] += 1
    else:
      ctr[c] = 1 
      char_order.append(c)
  for c in char_order:
    if ctr[c] == 1:
      return c
  return None

## Refactored Code:

```python
def first_non_repeating_character(input_string):
    """Return the first non-repeating character in the input string.

    Args:
        input_string: The string to search for the first non-repeating character.

    Returns:
        The first non-repeating character, or None if all characters repeat.
    """
    character_order = []
    character_counts = {}

    for character in input_string:
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1
            character_order.append(character)

    for character in character_order:
        if character_counts[character] == 1:
            return character

    return None
```

- Renamed variables to be more descriptive (e.g., `str1` to `input_string`, `ctr` to `character_counts`, `char_order` to `character_order`)
- Added a docstring to explain the function's purpose, arguments, and return value
- Maintained the same logic and behavior as the original implementation
- Kept the same return value (None) when no non-repeating character is found
- Preserved the order of operations and the use of two data structures (list for order, dict for counts)
- Ensured the function still passes all existing tests
- Improved readability by using consistent and meaningful variable names
- Maintained the same time complexity (O(n)) and space complexity (O(n))
