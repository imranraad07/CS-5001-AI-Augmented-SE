def remove_column(list1, n):
    """Remove the nth column from each row in the 2D list."""
    for row in list1:
        del row[n]
    return list1
