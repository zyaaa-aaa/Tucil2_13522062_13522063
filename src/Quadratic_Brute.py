import matplotlib.pyplot as plt
import numpy as np
import time
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

def quadratic_bezier(p0, p1, p2, num_points):
    points = []
    for t in np.linspace(0, 1, num_points):
        x = (1 - t)**2 * p0.x + 2 * (1 - t) * t * p1.x + t**2 * p2.x
        y = (1 - t)**2 * p0.y + 2 * (1 - t) * t * p1.y + t**2 * p2.y
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