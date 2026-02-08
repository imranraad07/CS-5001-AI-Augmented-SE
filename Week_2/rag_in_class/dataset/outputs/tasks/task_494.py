def binary_to_integer(test_tup):
    binary_str = "".join(str(ele) for ele in test_tup)
    integer_value = int(binary_str, 2)
    return str(integer_value)
