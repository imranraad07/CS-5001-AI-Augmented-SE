def remove_elements(list1, list2):
    """Remove elements from list1 that are present in list2.

    Args:
        list1: The list from which elements will be removed.
        list2: The list containing elements to be removed from list1.

    Returns:
        A new list containing only elements from list1 that are not in list2.
    """
    result = [x for x in list1 if x not in list2]
    return result
