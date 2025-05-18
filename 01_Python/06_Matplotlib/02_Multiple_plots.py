import matplotlib.pyplot as plt
import numpy as np

x  = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.figure(figsize=(10, 8))

# plt.subplot( nrows , ncols , index )

plt.subplot(2, 2, 1)     
plt.plot(x, y1, 'g')
plt.title('Plot 1')

plt.subplot(2, 2, 2)     
plt.plot(x, y2, 'r')
plt.title('Plot 2')

plt.subplot(2, 2, 3)        
plt.plot(x, np.tan(x), 'green')
plt.ylim(-5, 5)             
plt.title('tan(x)')

plt.tight_layout()
plt.show()
