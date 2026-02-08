def remove_elements(list1, list2):
    """Remove elements from list1 that are present in list2."""
    result = [x for x in list1 if x not in list2]
    return result
