def rgb_to_hsv(r, g, b):
    # Normalize RGB values to the range [0, 1]
    r_normalized = r / 255.0
    g_normalized = g / 255.0
    b_normalized = b / 255.0

    # Find the maximum and minimum values among the normalized RGB components
    max_value = max(r_normalized, g_normalized, b_normalized)
    min_value = min(r_normalized, g_normalized, b_normalized)
    delta = max_value - min_value

    # Calculate Hue (H)
    if max_value == min_value:
        hue = 0
    elif max_value == r_normalized:
        hue = (60 * ((g_normalized - b_normalized) / delta) + 360) % 360
    elif max_value == g_normalized:
        hue = (60 * ((b_normalized - r_normalized) / delta) + 120) % 360
    elif max_value == b_normalized:
        hue = (60 * ((r_normalized - g_normalized) / delta) + 240) % 360

    # Calculate Saturation (S)
    saturation = 0 if max_value == 0 else (delta / max_value) * 100

    # Calculate Value (V)
    value = max_value * 100

    return hue, saturation, value
