import numpy as np
import matplotlib.pyplot as plt

def main():
    plt.figure(figsize=(6,6))
    
    plot_approximation() # Plot the Marching Cubes Approximation
    plot_actual_function(heart) # Plot the Original Heart Function
    
    plt.title('Marching Cubes Approximation of Heart Shape')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_approximation():

    edges = generate_contour_edges(heart)

    for edge in edges:
        plt.plot([edge.p0.x, edge.p1.x], [edge.p0.y, edge.p1.y], 'b-')

def plot_actual_function(f):
    # Create a meshgrid for x and y
    x_values = np.linspace(-3, 3, 100)
    y_values = np.linspace(-3, 3, 100)
    x_mesh, y_mesh = np.meshgrid(x_values, y_values)

    # Evaluate the function for the entire meshgrid
    z_values = f(x_mesh, y_mesh)

    # Plot the original function's contour line
    plt.contour(x_mesh, y_mesh, z_values, levels=[0], colors='r', linestyles='dashed')

def heart(x, y):
    return (x**2 + y**2 - 1)**3 - x**2 * y**3

# Generates contour edges for a given function f using the Marching Cubes algorithm
def generate_contour_edges(f, xmin=-3, xmax=3, ymin=-3, ymax=3):
    edges = []
    for x in range(xmin, xmax):
        for y in range(ymin, ymax):
            edges.extend(process_single_grid_cell(f, x, y))
    return edges

# Calculates the distance from a point (x, y) to a circle with radius 2.5 centered at the origin
def distance_from_circle_boundary(x, y):
    distance_from_origin = np.sqrt(x**2 + y**2)
    return 2.5 - distance_from_origin

# Helper function to find the adapted value between two points (v0, v1) in Marching Cubes
def adapt(v0, v1):
    return -v0 / (v1 - v0)

# Class representing an edge with start and end points
class Edge:
    def __init__(self, p0, p1):
        self.p0 = p0
        self.p1 = p1

    def swap(self, condition):
        return Edge(self.p1, self.p0) if condition else self

# Class representing a 2D vector with coordinates (x, y)
class V2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Processes a single grid cell and returns edges that approximate the boundary for that cell
def process_single_grid_cell(f, x, y):
    x0y0 = f(x + 0.0, y + 0.0)
    x0y1 = f(x + 0.0, y + 1.0)
    x1y0 = f(x + 1.0, y + 0.0)
    x1y1 = f(x + 1.0, y + 1.0)
    case = ((1 if x0y0 > 0 else 0) +
            (2 if x0y1 > 0 else 0) +
            (4 if x1y0 > 0 else 0) +
            (8 if x1y1 > 0 else 0))
    
    if case == 0 or case == 15:
        return []
    if case == 1 or case == 14:
        return [Edge(V2(x+0+adapt(x0y0, x1y0), y), V2(x+0, y+adapt(x0y0, x0y1))).swap(case == 14)]
    if case == 2 or case == 13:
        return [Edge(V2(x + 0, y + adapt(x0y0, x0y1)), V2(x + adapt(x0y1, x1y1), y + 1)).swap(case == 11)]
    if case == 4 or case == 11:
        return [Edge(V2(x + 1, y + adapt(x1y0, x1y1)), V2(x + adapt(x0y0, x1y0), y + 0)).swap(case == 13)]
    if case == 8 or case == 7:
        return [Edge(V2(x+adapt(x0y1, x1y1), y+1), V2(x+1, y+adapt(x1y0, x1y1))).swap(case == 7)]
    if case == 3 or case == 12:
        return [Edge(V2(x+adapt(x0y0, x1y0), y+0), V2(x+adapt(x0y1, x1y1), y+1)).swap(case == 10)]
    if case == 5 or case == 10:
        return [Edge(V2(x+0, y+adapt(x0y0, x0y1)), V2(x+1, y+adapt(x1y0, x1y1))).swap(case == 5)]
    if case == 9:
        return [Edge(V2(x + 0 + adapt(x0y0, x1y0), y), V2(x + 0, y + adapt(x0y0, x0y1))),
                Edge(V2(x + adapt(x0y1, x1y1), y + 1), V2(x + 1, y + adapt(x1y0, x1y1)))]
    if case == 6:
        return [Edge(V2(x+1, y+adapt(x1y0, x1y1)), V2(x+adapt(x0y0, x1y0), y+0)),
                Edge(V2(x+0, y+adapt(x0y0, x0y1)), V2(x+adapt(x0y1, x1y1), y+1))]

    assert False, "All cases exhausted"

if __name__ == "__main__":
    main()