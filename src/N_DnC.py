from collections import namedtuple

# inisialisasi new tuple dengan jenis point (x, y)
Point = namedtuple("Point", ["x", "y"])

# mencari midpoint di antara 2 titik
def mid_point(point1: Point, point2: Point) -> Point:
        return Point((point1.x + point2.x) / 2, (point1.y + point2.y) / 2)

# mencari titik-titik pembentuk kurva bezier dengan konsep midpoint algorithm
def dnc_bezier_curve(control_points: list[Point], iterations: int) -> list[Point]:
    initial = control_points.copy()
    titik_awal = control_points[0]
    titik_akhir = control_points[-1]

    # recursion base
    if iterations == 0 :
        return initial
    elif iterations == 1 :
        initial = control_points.copy()
        for i in range(len(control_points)) :
            if (i != len(control_points) - 1):
                temp = []
                for j in range(len(initial) - 1):
                    mid = mid_point(initial[j], initial[j+1])
                    temp.append(mid)
                initial = temp
        mid_points = initial[0]

        return [titik_awal, mid_points, titik_akhir]
    
    # recursion iteration
    else :
        kanan = [titik_akhir]
        kiri = [titik_awal]
        
        for i in range(len(control_points)):
            if (i != len(control_points) - 1):
                temp = []
                for j in range(len(initial) - 1):
                    mid = mid_point(initial[j], initial[j+1])
                    temp.append(mid)
                kanan.insert(0, temp[-1])
                kiri.append(temp[0])
                initial = temp
        mid_points = initial[0]
        
        # divide bagi kiri, tengah, kanan
        left = dnc_bezier_curve(kiri, iterations - 1)
        middle = [mid_points]
        right = dnc_bezier_curve(kanan, iterations - 1)
        
        # conquer (gabungin)
        return left + middle + right