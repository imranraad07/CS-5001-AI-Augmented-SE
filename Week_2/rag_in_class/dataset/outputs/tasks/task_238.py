def number_of_substrings(input_string):
    string_length = len(input_string)
    return int(string_length * (string_length + 1) / 2)
