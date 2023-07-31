import numpy as np
import matplotlib.pyplot as plt

# Main function, entry point of program.
def main():
    edges = generate_contour_edges(distance_from_circle_boundary)
    plt.figure(figsize=(6,6))
    for edge in edges:
        plt.plot([edge.p0.x, edge.p1.x], [edge.p0.y, edge.p1.y], 'b-')

    plt.title('Marching Cubes Approximation of Circle')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.grid(True)
    plt.show()

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
        return [Edge(V2(x, y+0.5), V2(x+0.5, y)).swap(case == 14)]
    if case == 2 or case == 13:
        return [Edge(V2(x + 0.5, y + 1), V2(x + 0, y + 0.5)).swap(case == 13)]
    if case == 4 or case == 11:
        return [Edge(V2(x + 1, y + 0.5), V2(x + 0.5, y + 0)).swap(case == 11)]
    if case == 8 or case == 7:
        return [Edge(V2(x+0.5, y+1), V2(x+1, y+0.5)).swap(case == 7)]
    if case == 3 or case == 12:
        return [Edge(V2(x+0.5, y+0), V2(x+0.5, y+1)).swap(case == 12)]
    if case == 5 or case == 10:
        return [Edge(V2(x+0, y+0.5), V2(x+1, y+0.5)).swap(case == 10)]
    if case == 6:
        return [Edge(V2(x+1, y+0.5), V2(x+0.5, y+0)),
                Edge(V2(x+0, y+0.5), V2(x+0.5, y+1))]
    if case == 9:
        return [Edge(V2(x + 0.5, y), V2(x + 0, y + 0.5)),
                Edge(V2(x + 0.5, y + 1), V2(x + 1, y + 0.5))]

    assert False, "All cases exhausted"

if __name__ == "__main__":
    main()