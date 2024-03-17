import numpy as np
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

def quadratic_bezier_brute(point1, point2, point3, num_points):
    points = []
    for t in np.linspace(0, 1, num_points):
        x = (1 - t)**2 * point1.x + 2 * (1 - t) * t * point2.x + t**2 * point3.x
        y = (1 - t)**2 * point1.y + 2 * (1 - t) * t * point2.y + t**2 * point3.y
        points.append(Point(x, y))
    return points