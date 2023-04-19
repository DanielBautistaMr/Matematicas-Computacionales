import matplotlib.pyplot as plt
import numpy as np



x = np.array([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
y = np.array([4.2,6.5,7.5,8,8.5,8.8,9,9.1])


m, b = np.polyfit(x, y, 1)



print("a1=", m.round(6))
print("a0=", b.round(6))

plt.scatter(x,y)
plt.plot(x,y,'g', alpha=0.8)
plt.grid()
plt.show()