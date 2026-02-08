def first_non_repeating_character(str1):
    char_order = []
    character_counts = {}

    for character in str1:
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1
            char_order.append(character)

    for character in char_order:
        if character_counts[character] == 1:
            return character

    return None
