import numpy as np
import matplotlib.pyplot as plt

def distance_from_circle(x,y):
    return 2.5 - np.sqrt((x**2 + y**2)) 

def main():
    # Create a grid of x, y points
    x = np.linspace(-3, 3, 400)
    y = np.linspace(-3, 3, 400)
    X, Y = np.meshgrid(x, y)

    # Compute the value of the circle function at each point
    Z = circle(X, Y)

    # Create a contour plot
    plt.figure(figsize=(6,6))
    contour = plt.contour(X, Y, Z, levels=[0], colors='b')

    # Add a dot at each whole coordinate
    for i in range(-3, 4):
        for j in range(-3, 4):
            if distance_from_circle(i, j) > 0:
                plt.plot(i, j, 'ro')
            elif distance_from_circle(i, j) < 0:
                plt.plot(i, j, 'bo')

    plt.title('Plot of Circle Function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

def circle(x, y):
    return 2.5 - np.sqrt(x**2 + y**2)

if __name__ == "__main__":
    main()
