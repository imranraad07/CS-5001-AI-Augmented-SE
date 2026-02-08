def parabola_vertex(a, b, c):
    x_coordinate = -b / (2 * a)
    y_coordinate = ((4 * a * c) - (b * b)) / (4 * a)
    vertex = (x_coordinate, y_coordinate)
    return vertex
