from N_DnC import dnc_bezier_curve, Point
from N_BF import bf_bezier_curve
from Visualisation import *
from matplotlib.animation import FuncAnimation
import time

print("=======================================")
print("              Bezier Curve             ")
print("=======================================")
print("1. Nth Degree")
print("2. Exit")
print("=======================================")
choice = int(input("Choice: "))
print("=======================================")
stop_program = False
while(stop_program == False):
    while(choice != 1 and choice != 2):
        print("=======================================")
        print("              Bezier Curve             ")
        print("=======================================")
        print("1. Nth Degree")
        print("2. Exit")
        print("=======================================")
        choice = int(input("Choice: "))
        print("=======================================")

    if(choice == 1):
        jumlah_titik = int(input("Masukkan jumlah titik: "))

        print("Input titik (x dan y dipisahkan oleh spasi). Titik dimulai dengan titik awal dan diakhiri dengan titik akhir (berurutan).")
        print("Contoh: 0 0")

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
        num_points = 2 ** iteration + 1
          
        start_dnc = time.time()
        dnc_points = dnc_bezier_curve(control_points, iteration)
        end_dnc = time.time()

        start_bf = time.time()
        bf_points = bf_bezier_curve(control_points, num_points)
        end_bf = time.time()

        print()
        print("Waktu eksekusi Divide and Conquer:", (end_dnc-start_dnc)*1000, "ms")
        print("Waktu eksekusi Brute Force:", (end_bf-start_bf)*1000, "ms")

        if (end_bf-start_bf) > (end_dnc-start_dnc):
            print("Divide and Conquer lebih cepat dari Brute Force sebesar", (end_bf-start_bf)-(end_dnc-start_dnc)*1000, "ms")
        else:
            print("Brute Force lebih cepat dari Divide and Conquer sebesar", (end_dnc-start_dnc)-(end_bf-start_bf)*1000, "ms")
        
        # Animation
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        ani = FuncAnimation(fig, animate, frames=range(iteration + 1),fargs=(control_points, ax1, ax2), interval=350,repeat=False)
        plt.show()

        # Final Result Visualisation
        plot_dnc_bezier_curve(control_points, jumlah_titik)
        plot_bf_bezier_curve(control_points, num_points)

        print("=======================================")
        print("              Bezier Curve             ")
        print("=======================================")
        print("1. Nth Degree")
        print("2. Exit")
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