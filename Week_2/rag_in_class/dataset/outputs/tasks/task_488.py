import math

def area_pentagon(a):
    """Calculate the area of a regular pentagon with side length a."""
    area = (math.sqrt(5 * (5 + 2 * math.sqrt(5))) * pow(a, 2)) / 4.0
    return area
