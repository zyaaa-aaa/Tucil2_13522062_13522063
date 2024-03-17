import matplotlib.pyplot as plt
import numpy as np
from N_DnC import *

# menunjukkan bezier curve yang quadratic
def plot_quadratic_bezier(dnc_points: List[Point], brute_points: List[Point]) -> None:
    plt.figure(1)
    dnc = np.array(dnc_points)
    plt.plot(dnc[:, 0], dnc[:, 1], marker='o', linestyle='-')
    plt.title('Divide and Conquer Quadratic Bezier Curve Visualization')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)

    plt.figure(2)
    brute = np.array(brute_points)
    plt.plot(brute[:, 0], brute[:, 1], marker='o', linestyle='-')
    plt.title('Brute Force Quadratic Bezier Curve Visualization')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)

    plt.show()

# menunjukkan bezier curve yang memiliki derajat n
def plot_n_bezier(dnc_points: List[Point], jumlah_titik: int) -> None:
    plt.figure(1)
    dnc = np.array(dnc_points)
    plt.plot(dnc[:, 0], dnc[:, 1], marker='o', linestyle='-')
    plt.title('Divide and Conquer '+str(jumlah_titik-1)+' Degree Bezier Curve Visualization')
    plt.grid(True)
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.show() 