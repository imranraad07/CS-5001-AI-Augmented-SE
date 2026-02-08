def decimal_To_Binary(N):
    binary_number = 0
    position = 0

    while N != 0:
        remainder = N % 2
        place_value = 10 ** position
        binary_number += remainder * place_value
        N = N // 2
        position += 1

    return binary_number
