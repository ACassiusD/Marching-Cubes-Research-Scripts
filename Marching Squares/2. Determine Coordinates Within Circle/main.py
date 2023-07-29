import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the distance from a point (x, y) to a circle with radius 2.5 centered at the origin
def distance_from_circle(x,y):
    return 2.5 - np.sqrt((x**2 + y**2)) 

def main():
    # Create a grid of x, y points using linspace and meshgrid
    x = np.linspace(-3, 3, 400)
    y = np.linspace(-3, 3, 400)
    X, Y = np.meshgrid(x, y)

    # Compute the value of the circle function at each point using the circle function
    Z = distance_from_circle(X, Y)

    # Create a contour plot to visualize the circle (where the distance to the circle's radius is zero)
    plt.figure(figsize=(6,6))
    contour = plt.contour(X, Y, Z, levels=[0], colors='b')

    # Iterate through whole coordinates in the range [-3, 3] for both x and y
    for i in range(-3, 4):
        for j in range(-3, 4):
            dist = distance_from_circle(i, j)
            # If the distance from the circle is positive, the point is outside the circle and is plotted with a red dot
            if dist > 0:
                plt.plot(i, j, 'ro')
            # If the distance from the circle is negative, the point is inside the circle and is plotted with a blue dot
            elif dist < 0:
                plt.plot(i, j, 'bo')

    # Add labels and grid to the plot for better visualization
    plt.title('Determine Coordinates Within Circle Function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    # Display the plot
    plt.show()

# Function to calculate the distance from a point (x, y) to a circle with radius 2.5 centered at the origin
def distance_from_circle_boundary(x, y):
    # Calculate the Euclidean distance from the origin to the point (x, y)
    distance_from_origin = np.sqrt(x**2 + y**2)
    
    # Return the difference between the circle's radius and the distance from the origin
    return 2.5 - distance_from_origin

# Entry point of the program: call the main function if the script is run as the main program
if __name__ == "__main__":
    main()