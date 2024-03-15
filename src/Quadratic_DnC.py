from typing import List
from collections import namedtuple
import matplotlib.pyplot as plt
import numpy as np
import time

Point = namedtuple("Point", ["x", "y"])

def bezier_curve(ctrl1: Point, ctrl2: Point, ctrl3: Point, iterations: int) -> List[Point]:
    bezier_points = []
    init_points = [ctrl1, ctrl2, ctrl3]

    def recalculate(ctrl1: Point, ctrl2: Point, ctrl3: Point) -> None:
        init_points.clear()
        init_points.extend([ctrl1, ctrl2, ctrl3])
        create_bezier(ctrl1, ctrl2, ctrl3)

    def create_bezier(ctrl1: Point, ctrl2: Point, ctrl3: Point) -> None:
        nonlocal bezier_points
        bezier_points.clear()
        bezier_points.append(ctrl1)
        populate_bezier_points(ctrl1, ctrl2, ctrl3, 0)
        bezier_points.append(ctrl3)

    def populate_bezier_points(ctrl1: Point, ctrl2: Point, ctrl3: Point, current_iteration: int) -> None:
        nonlocal bezier_points
        if current_iteration < iterations:
            mid_point1 = mid_point(ctrl1, ctrl2)
            mid_point2 = mid_point(ctrl2, ctrl3)
            mid_point3 = mid_point(mid_point1, mid_point2)
            current_iteration += 1
            populate_bezier_points(ctrl1, mid_point1, mid_point3, current_iteration)
            bezier_points.append(mid_point3)
            populate_bezier_points(mid_point3, mid_point2, ctrl3, current_iteration)

    def mid_point(control_point1: Point, control_point2: Point) -> Point:
        return Point(
            (control_point1.x + control_point2.x) / 2,
            (control_point1.y + control_point2.y) / 2
        )

    recalculate(ctrl1, ctrl2, ctrl3)
    return bezier_points

def plot_bezier_curve(bezier_points: List[Point]) -> None:
    points = np.array(bezier_points)
    plt.plot(points[:, 0], points[:, 1], marker='o', linestyle='-')
    plt.title('Bezier Curve Visualization')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

x1, y1 = input("Masukkan titik kontrol 1: ").split()
x2, y2 = input("Masukkan titik kontrol 2 (titik kontrol tengah): ").split()
x3, y3 = input("Masukkan titik kontrol 3: ").split()
iterations = int(input("Masukkan jumlah iterasi: "))

ctrl1 = Point(float(x1), float(y1))
ctrl2 = Point(float(x2), float(y2)) #control point center
ctrl3 = Point(float(x3), float(y3))
# iterations = 3

start_time = time.time()
points = bezier_curve(ctrl1, ctrl2, ctrl3, iterations)
end_time = time.time()
print(end_time-start_time)
plot_bezier_curve(points)