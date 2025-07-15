import matplotlib.pyplot as plt
import numpy as np

# Generate 100 points between 0 and 10
x = np.linspace(0, 10, 100)  
# Compute sine function values
y = np.sin(x)  

# Plot sine wave
plt.plot(x, y, label="Sine Wave")  
plt.xlabel("X-axis")  # Label for x-axis
plt.ylabel("Y-axis")  # Label for y-axis
plt.title("Line Plot")  # Title of the plot
plt.legend()  # Display legend
plt.show()  # Show the plot