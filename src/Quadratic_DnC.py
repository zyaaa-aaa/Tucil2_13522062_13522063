from typing import List
from collections import namedtuple
import matplotlib.pyplot as plt
import numpy as np

Point = namedtuple("Point", ["x", "y"])

def quadratic_bezier_curve(point1: Point, point2: Point, point3: Point, iteration: int) -> List[Point]:
    bezier_points = []
    initial = [point1, point2, point3]

    # menambahkan titik awal dan titik akhir ke bezier_points dan juga menambahkan midpoint di antara control points
    def create_bezier(point1: Point, point2: Point, point3: Point) -> None:
        nonlocal bezier_points
        bezier_points.clear()
        bezier_points.append(point1)
        line_midpoint(point1, point2, point3, 0)
        bezier_points.append(point3)

    # mencari midpoint di antara control points secara rekursif dan mencarinya sebanyak jumlah iterasi
    def line_midpoint(point1: Point, point2: Point, point3: Point, current_iteration: int) -> None:
        nonlocal bezier_points
        if current_iteration < iteration:
            mid_point1 = mid_point(point1, point2)
            mid_point2 = mid_point(point2, point3)
            mid_point3 = mid_point(mid_point1, mid_point2)
            current_iteration += 1
            line_midpoint(point1, mid_point1, mid_point3, current_iteration)
            bezier_points.append(mid_point3)
            line_midpoint(mid_point3, mid_point2, point3, current_iteration)

    # mencari midpoint di antara 2 titik
    def mid_point(point1: Point, point2: Point) -> Point:
        return Point((point1.x + point2.x) / 2, (point1.y + point2.y) / 2)

    initial.clear()
    initial.extend([point1, point2, point3])
    create_bezier(point1, point2, point3)
    return bezier_points

def plot_bezier_curve(bezier_points: List[Point]) -> None:
    points = np.array(bezier_points)
    plt.plot(points[:, 0], points[:, 1], marker='o', linestyle='-')
    plt.title('Divide and Conquer Bezier Curve Visualization')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()