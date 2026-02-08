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
