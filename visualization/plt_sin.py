from matplotlib import pyplot as plt
import numpy as np
from math import pi

x = np.arange(0, pi*2, 0.05)
y = np.sin(x)
plt.plot(x,y)
plt.xlabel("angle")
plt.ylabel("sine")
plt.title('sine wave')
plt.show()