def count_uppercase_letters(input_string):
    """Count the number of uppercase letters in the input string."""
    count = 0
    for char in input_string:
        if 'A' <= char <= 'Z':
            count += 1
    return count
