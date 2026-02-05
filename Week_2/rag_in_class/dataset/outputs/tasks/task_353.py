def remove_column(matrix, column_index):
    """Remove the specified column from each row in the matrix.

    Args:
        matrix: A list of lists where each inner list represents a row.
        column_index: The index of the column to remove from each row.

    Returns:
        The matrix with the specified column removed from each row.
    """
    for row in matrix:
        del row[column_index]
    return matrix
