import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data using NumPy
x = np.linspace(0, 10, 100)  # Generate 100 points between 0 and 10
y = np.sin(x)                 # Compute the sine of each point

# Plot the data using Matplotlib
plt.plot(x, y, label='sin(x)')  # Plot x versus y with label 'sin(x)'
plt.xlabel('x')                 # Label for x-axis
plt.ylabel('y')                 # Label for y-axis
plt.title('Sine Function')      # Title of the plot
plt.legend()                    # Show legend
plt.grid(True)                  # Show grid
plt.show()                      # Display the plot

