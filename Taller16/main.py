import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,2,3,4,5,6,7])
y = np.array([3.5,2.5,3,1.5,2,1.3,1,0.3])


m, b = np.polyfit(x, y, 1)


print("a1=", m.round(6))
print("a0=", b.round(6))

plt.scatter(x,y)
plt.plot(x,y,'g', alpha=0.1)
plt.plot(x,m*x+b, 'r--')
plt.grid()
plt.show()