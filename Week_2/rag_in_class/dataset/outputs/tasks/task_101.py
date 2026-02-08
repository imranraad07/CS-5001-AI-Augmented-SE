def kth_element(arr, n, k):
    # Perform bubble sort on the array
    for i in range(n):
        for j in range(0, n - i - 1):
            # Swap elements if they are in the wrong order
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] == arr[j + 1], arr[j]
    # Return the k-th smallest element (1-based index)
    return arr[k - 1]
