from Quadratic_Brute import quadratic_bezier, plot_curve
from Quadratic_DnC import bezier_curve, plot_bezier_curve, Point
import time

print("=======================================")
print("              Bezier Curve             ")
print("=======================================")
print("1. Quadratic")
print("2. Exit")
print("=======================================")
choice = int(input("Choice: "))
print("=======================================")
stop_program = False
while(1 <= choice <= 2 and stop_program == False):
    if(choice == 1):
        x1, y1 = input("Masukkan titik kontrol 1: ").split()
        x2, y2 = input("Masukkan titik kontrol 2 (titik kontrol tengah): ").split()
        x3, y3 = input("Masukkan titik kontrol 3: ").split()
        iterations = int(input("Masukkan jumlah iterasi: "))

        ctrl1 = Point(float(x1), float(y1))
        ctrl2 = Point(float(x2), float(y2)) #control point center
        ctrl3 = Point(float(x3), float(y3))

        num_points = 2**iterations + 1

        start_dnc = time.time()
        dnc_points = bezier_curve(ctrl1, ctrl2, ctrl3, iterations)
        end_dnc = time.time()

        start_brute = time.time()
        brute_points = quadratic_bezier(ctrl1, ctrl2, ctrl3, num_points)
        end_brute = time.time()

        print()
        print("Waktu eksekusi Divide and Conquer:", (end_dnc-start_dnc)*1000, "ms")
        print("Waktu eksekusi Brute Force:", (end_brute-start_brute)*1000, "ms")

        difference = abs((end_dnc-start_dnc)*1000 - (end_brute-start_brute)*1000)
        if(difference >= 0):
            print("Metode Divide and Conquer lebih cepat sebesar", difference, "ms")
        else:
            print("Metode Brute Force lebih cepat sebesar", difference, "ms")

        plot_bezier_curve(dnc_points)
        plot_curve(brute_points)
        print("=======================================")
        choice = int(input("Choice: "))
        print("=======================================")
    if(choice == 2):
        stop_program = True
        print("=======================================")
        print("              Thank You!               ")
        print("=======================================")
        print("               13522062                ")
        print("               13522063                ")
        print("=======================================")