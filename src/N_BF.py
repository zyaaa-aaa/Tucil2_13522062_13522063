from typing import List, Tuple
import matplotlib.pyplot as plt
import numpy as np

Point_N = Tuple[float, float]

def interpolate(control_points: List[Point_N], t: float) -> Point_N:
    if len(control_points) == 1:
        return control_points[0]
    
    # Interpolate between 2 control points
    interpolated_points = []
    for i in range(len(control_points) - 1):
        x = (1 - t) * control_points[i][0] + t * control_points[i + 1][0]
        y = (1 - t) * control_points[i][1] + t * control_points[i + 1][1]
        interpolated_points.append((x, y))
    
    return interpolate(interpolated_points, t)

def bf_bezier_curve(control_points: List[Point_N], num_points: int) -> List[Point_N]:
    bezier_points = []
    for i in range(num_points):
        t = i / (num_points - 1)
        bezier_point = interpolate(control_points, t)
        bezier_points.append(bezier_point)
    
    return bezier_points