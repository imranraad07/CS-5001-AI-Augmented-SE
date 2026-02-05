def frequency_of_largest(n, arr):
    """Return the frequency of the largest element in the array."""
    if n == 0:
        return 0

    max_value = arr[0]
    frequency = 1

    for i in range(1, n):
        if arr[i] > max_value:
            max_value = arr[i]
            frequency = 1
        elif arr[i] == max_value:
            frequency += 1

    return frequency
