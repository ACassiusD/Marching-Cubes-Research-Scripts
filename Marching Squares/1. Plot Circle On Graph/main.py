import matplotlib.pyplot as plt
import numpy as np

def main():
    # Create a grid of x and y points ranging from -3 to 3 with 400 points in between
    x = np.linspace(-3, 3, 400)
    y = np.linspace(-3, 3, 400)
    
    # Create a meshgrid from the x and y values, which will allow us to evaluate the function over a 2D grid
    X, Y = np.meshgrid(x, y)

    # Compute the distance to the circle's radius for each (x, y) point in the grid
    Z = distance_to_circle_radius(X, Y)

    # Create a contour plot, which will draw the circle where the distance to the radius is zero
    plt.figure(figsize=(6,6))
    plt.contour(X, Y, Z, levels=[0], colors='b')
    
    # Add labels and title to the plot
    plt.title('Plot of Circle Function')
    plt.xlabel('x')
    plt.ylabel('y')
    
    # Show a grid on the plot for better visualization
    plt.grid(True)
    
    # Display the plot
    plt.show()

# Function to calculate the distance from a point (x, y) to a circle with radius 2.5 centered at the origin
def distance_to_circle_radius(x, y):
    # Calculate the Euclidean distance from the origin to the point (x, y)
    distance_from_origin = np.sqrt(x**2 + y**2)
    
    # Return the difference between the circle's radius and the distance from the origin
    return 2.5 - distance_from_origin

# If this script is run as the main program, call the main function
if __name__ == "__main__":
    main()




