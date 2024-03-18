from N_DnC import dnc_bezier_curve, Point
from N_BF import bf_bezier_curve
from Visualisation import *
from Input import *
from matplotlib.animation import FuncAnimation
import time
import numpy as np

choice = input_main_menu()
stop_program = False
while(stop_program == False):
    while(choice != 1 and choice != 2):
        choice = input_main_menu()

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

        dnc_time = np.float16(end_dnc-start_dnc)*1000
        bf_time = np.float16(end_bf-start_bf)*1000

        print()
        print("Waktu eksekusi Divide and Conquer:", dnc_time, "ms")
        print("Waktu eksekusi Brute Force:", bf_time, "ms")

        if bf_time > dnc_time:
            print("Divide and Conquer lebih cepat dari Brute Force sebesar", bf_time-dnc_time, "ms")
        else:
            print("Brute Force lebih cepat dari Divide and Conquer sebesar", dnc_time-bf_time, "ms")
        
        # Animation
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        ani = FuncAnimation(fig, animate, frames=range(iteration + 1), fargs=(control_points, ax1, ax2), interval=350, repeat=False)
        plt.show()

        # Final Result Visualisation
        vis_choice = input_visualisation_menu()
        while(vis_choice != 1 and vis_choice != 2 and vis_choice != 3):
            vis_choice = input_visualisation_menu()

        while(vis_choice == 1 or vis_choice == 2):
            if(vis_choice == 1):
                plot_dnc_bezier_curve(control_points, iteration)
                vis_choice = input_visualisation_menu()

            if(vis_choice == 2):
                plot_bf_bezier_curve(control_points, num_points)
                vis_choice = input_visualisation_menu()
                
        choice = input_main_menu()

    if(choice == 2):
        stop_program = True
        print("=======================================")
        print("              Thank You!               ")
        print("=======================================")
        print("               13522062                ")
        print("               13522063                ")
        print("=======================================")