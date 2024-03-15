import matplotlib.pyplot as plt
import numpy as np
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

def quadratic_bezier(point1, point2, point3, num_points):
    points = []
    for t in np.linspace(0, 1, num_points):
        x = (1 - t)**2 * point1.x + 2 * (1 - t) * t * point2.x + t**2 * point3.x
        y = (1 - t)**2 * point1.y + 2 * (1 - t) * t * point2.y + t**2 * point3.y
        points.append(Point(x, y))
    return points

def plot_curve(points):
    points = np.array(points)
    plt.plot(points[:, 0], points[:, 1], marker='o', linestyle='-')
    plt.title('Brute Force Bézier Curve Visualization')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()