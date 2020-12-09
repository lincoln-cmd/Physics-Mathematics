import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure()
ax = plt.axes(projection = '3d')
z = np.linspace(0, 1, 100)
x = z * np.sin(20 * z)
y = z * np.cos(20 * z)
ax.plot3D(x, y, z, 'gray')
ax.set_title('3D line plot')
plt.show()

ax2 = plt.axes(projection = '3d')
z2 = np.linspace(0, 1, 100)
x2 = z * np.sin(20 * z2)
y2 = z * np.cos(20 * z2)
c = x2 + y2
ax2.scatter(x, y, z, c = c)
ax2.set_title('3D Scatter plot')
plt.show()