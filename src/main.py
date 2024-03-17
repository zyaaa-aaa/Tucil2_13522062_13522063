from Quadratic_Brute import quadratic_bezier_brute
from N_DnC import bezier_curve, Point
from Visualisation import *
import time

print("=======================================")
print("              Bezier Curve             ")
print("=======================================")
print("1. Quadratic")
print("2. Nth Degree")
print("3. Exit")
print("=======================================")
choice = int(input("Choice: "))
print("=======================================")
stop_program = False
while(stop_program == False):
    while(choice != 1 and choice != 2):
        choice = int(input("Choice: "))
        print("=======================================")
    if(choice == 1 or choice == 2):
        print("Input titik (x dan y dipisahkan oleh spasi). Titik dimulai dengan titik awal dan diakhiri dengan titik akhir (berurutan).")
        print("Contoh: 0 0")
        if(choice == 1):
            jumlah_titik = 3
        if (choice == 2):
            jumlah_titik = int(input("Masukkan jumlah titik: "))
        control_points = []
        for i in range(jumlah_titik):
            while True:
                try:
                    x, y = input(f"Masukkan titik {i+1}: ").split()
                    temp_titik = Point(float(x), float(y))
                    control_points.append(temp_titik)
                    break  # loop berhenti ketika sudah input benar
                except ValueError:
                    print("Input harus berupa dua angka yang dipisahkan oleh spasi.")
                    continue  # ulangi minta input
        iteration = int(input("Masukkan jumlah iterasi: "))

        if (choice == 1):
            num_points = 2 ** iteration + 1

            start_dnc = time.time()
            dnc_points = bezier_curve(control_points, iteration)
            end_dnc = time.time()

            start_brute = time.time()
            brute_points = quadratic_bezier_brute(control_points[0], control_points[1], control_points[2], num_points)
            end_brute = time.time()

            print()
            print("Waktu eksekusi Divide and Conquer:", (end_dnc-start_dnc)*1000, "ms")
            print("Waktu eksekusi Brute Force:", (end_brute-start_brute)*1000, "ms")

            difference = (end_dnc-start_dnc)*1000 - (end_brute-start_brute)*1000
            if(difference >= 0):
                print("Metode Divide and Conquer lebih cepat sebesar", difference, "ms")
            else:
                print("Metode Brute Force lebih cepat sebesar", abs(difference), "ms")

            plot_quadratic_bezier(dnc_points, brute_points)
        if(choice == 2):
            start_dnc = time.time()
            dnc_points = bezier_curve(control_points, iteration)
            end_dnc = time.time()

            print()
            print("Waktu eksekusi Divide and Conquer:", (end_dnc-start_dnc)*1000, "ms")
            plot_n_bezier(dnc_points, jumlah_titik)
        print("=======================================")
        choice = int(input("Choice: "))
        print("=======================================")
    if(choice == 3):
        stop_program = True
        print("=======================================")
        print("              Thank You!               ")
        print("=======================================")
        print("               13522062                ")
        print("               13522063                ")
        print("=======================================")