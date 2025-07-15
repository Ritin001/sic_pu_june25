import matplotlib.pyplot as plt
import random 
import numpy as np
# Create violin plot
data = [np.random.randn(100) for i in range(4)]
plt.violinplot(data)
plt.xlabel("Category")
plt.ylabel("Values")
plt.title("Violin Plot")
plt.show()