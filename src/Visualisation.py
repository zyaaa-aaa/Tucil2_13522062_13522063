import matplotlib.pyplot as plt
from N_DnC import *
from N_BF import *

def interpolate_vis(control_points: List[Point_N], t: float) -> Point_N:
    if len(control_points) == 1:
        return control_points[0]
    
    # Interpolate between 2 control points
    interpolated_points = []
    for i in range(len(control_points) - 1):
        x = (1 - t) * control_points[i][0] + t * control_points[i + 1][0]
        y = (1 - t) * control_points[i][1] + t * control_points[i + 1][1]
        interpolated_points.append((x, y))
        plt.plot
    
    x_values = [point[0] for point in interpolated_points]
    y_values = [point[1] for point in interpolated_points]
    plt.plot(x_values, y_values, '--')
    
    return interpolate(interpolated_points, t)

def bf_bezier_curve_interpolate_vis(control_points: List[Point_N], num_points: int) -> List[Point_N]:
    bezier_points = []
    for t in np.linspace(0, 1, num_points):
        bezier_point = interpolate_vis(control_points, t)
        bezier_points.append(bezier_point)
    
    return bezier_points

def plot_dnc_bezier_curve(control_points: List[Point], iteration: int):
    fig, ax = plt.subplots()

    # Bezier Curve per Iteration
    for i in range(iteration + 1):
        curve_points = dnc_bezier_curve(control_points, i)
        curve_x = [point.x for point in curve_points]
        curve_y = [point.y for point in curve_points]
        if i == 0:
            ax.plot(curve_x, curve_y, 'o-', label='Control Points')
        elif i != iteration:
            ax.plot(curve_x, curve_y, '--', label=f'Iteration {i}')
        else:
            ax.plot(curve_x, curve_y, 'o-', label=f'Divide and Conquer Bezier Curve')

    ax.legend()
    ax.set_title('Divide and Conquer Bezier Curve Visualization')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.grid(True)
    plt.show()

def plot_bf_bezier_curve(control_points: List[Point], num_points: int):
    bf_curve_points = bf_bezier_curve_interpolate_vis(control_points, num_points)

    # Control points
    control_x = [point[0] for point in control_points]
    control_y = [point[1] for point in control_points]
    plt.plot(control_x, control_y, 'o-', label='Control Points')

    # Bezier curve
    bf_curve_x = [point[0] for point in bf_curve_points]
    bf_curve_y = [point[1] for point in bf_curve_points]
    plt.plot(bf_curve_x, bf_curve_y, 'o-', label='Brute-Force Bezier Curve')


    plt.title('Brute-Force Bezier Curve Visualization')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()


def animate(iteration, control_points, ax1, ax2):
    ax1.clear()
    ax2.clear()

    for i in range(iteration + 1):
        curve_points = dnc_bezier_curve(control_points, i)
        curve_x = [point.x for point in curve_points]
        curve_y = [point.y for point in curve_points]
        if i == 0:
            ax1.plot(curve_x, curve_y, 'o-', label='Control Points')
        elif i != iteration:
            ax1.plot(curve_x, curve_y, '--', label=f'Iteration {i}')
        else:
            ax1.plot(curve_x, curve_y, 'o-', label=f'Divide and Conquer Bezier Curve')

    ax1.legend()
    ax1.set_title('Divide and Conquer Bezier Curve Visualization')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.grid(True)

    bf_curve_points = bf_bezier_curve_interpolate_vis(control_points, 2**iteration + 1)
    bf_curve_x = [point[0] for point in bf_curve_points]
    bf_curve_y = [point[1] for point in bf_curve_points]

    control_x = [point.x for point in control_points]
    control_y = [point.y for point in control_points]

    ax2.plot(control_x, control_y, 'o-', label='Control Points')
    ax2.plot(bf_curve_x, bf_curve_y, 'o-', label='Brute-Force Bezier Curve')

    ax2.legend()
    ax2.set_title('Brute-Force Bezier Curve Visualization')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.grid(True)