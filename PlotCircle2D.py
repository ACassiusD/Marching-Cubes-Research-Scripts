import numpy as np
import matplotlib.pyplot as plt

#f(x, y) = 2.5 - √(x^2 + y^2)
def main(x,y):
    # result = 2.5 - math.sqrt((x**2 + y**2)) 
    # print("The result of function(" + str(x) + ","+ str(y) + ") is... " + str(result))
    # Create a grid of x, y points
    x = np.linspace(-3, 3, 400)
    y = np.linspace(-3, 3, 400)
    X, Y = np.meshgrid(x, y)

    # Compute the value of the circle function at each point
    Z = circle(X, Y)

    # Create a contour plot
    plt.figure(figsize=(6,6))
    plt.contour(X, Y, Z, levels=[0], colors='b')
    plt.title('Plot of Circle Function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

def circle(x, y):
    return 2.5 - np.sqrt(x**2 + y**2)

if __name__ == "__main__":
    main(1,2.5)
