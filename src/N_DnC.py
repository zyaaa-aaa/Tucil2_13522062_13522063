from collections import namedtuple

# inisialisasi new tuple dengan jenis point (x, y)
Point = namedtuple("Point", ["x", "y"])

# mencari midpoint di antara 2 titik
def mid_point(point1: Point, point2: Point) -> Point:
        return Point((point1.x + point2.x) / 2, (point1.y + point2.y) / 2)

# mencari titik-titik pembentuk kurva bezier dengan konsep midpoint algorithm
def dnc_bezier_curve(control_points: list[Point], iterations: int) -> list[Point]:
    # Recursion base
    if iterations == 0:
        return control_points.copy()

    # Recursion iteration
    kanan = [control_points[-1]]
    kiri = [control_points[0]]
    temp_points = control_points.copy()

    for _ in range(len(control_points) - 1):
        temp = []
        for j in range(len(temp_points) - 1):
            mid = mid_point(temp_points[j], temp_points[j+1])
            temp.append(mid)
        kanan.insert(0, temp[-1])
        kiri.append(temp[0])
        temp_points = temp

    mid_points = temp_points[0]

    # Divide bagi kiri, tengah, kanan
    left = dnc_bezier_curve(kiri, iterations - 1)
    right = dnc_bezier_curve(kanan, iterations - 1)

    return left + [mid_points] + right