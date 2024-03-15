import matplotlib.pyplot as plt
import numpy as np
import time

def quadratic_bezier(p0, p1, p2, num_points):
    points = []
    for t in np.linspace(0, 1, num_points):
        x = (1 - t)**2 * p0[0] + 2 * (1 - t) * t * p1[0] + t**2 * p2[0]
        y = (1 - t)**2 * p0[1] + 2 * (1 - t) * t * p1[1] + t**2 * p2[1]
        points.append((x, y))
    return points

def plot_curve(points):
    points = np.array(points)
    plt.plot(points[:, 0], points[:, 1], marker='o', linestyle='-')
    plt.title('Quadratic Bézier Curve Visualization')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

# Control points
start_time = time.time()
p0 = (0, 4)
p1 = (0, 0) #control point center
p2 = (4, 0)

# Generate the quadratic Bézier curve points
curve_points = quadratic_bezier(p0, p1, p2, 9)
end_time = time.time()
print(end_time-start_time)

# Plot the curve
plot_curve(curve_points)