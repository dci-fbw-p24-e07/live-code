import matplotlib.pyplot as plt
import numpy as np

a = np.arange(15).reshape(3, 5)
print(f"Shape of array if {a.shape} ")

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
plt.savefig('simple_chart.png')
plt.show()