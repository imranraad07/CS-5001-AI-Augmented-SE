def sum_list(lst1, lst2):
    """Return a new list where each element is the sum of corresponding elements from lst1 and lst2."""
    return [lst1[i] + lst2[i] for i in range(len(lst1))]
