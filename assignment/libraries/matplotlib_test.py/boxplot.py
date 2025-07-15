import matplotlib.pyplot as plt
import random 
import numpy as np
data = [np.random.randn(100) for _ in range(4)]


# Create box plot
plt.boxplot(data, patch_artist=True)
plt.xlabel("Category")
plt.ylabel("Values")
plt.title("Box Plot")
plt.show()