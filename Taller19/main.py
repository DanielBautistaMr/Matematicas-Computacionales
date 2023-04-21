import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns



x = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
y = np.array([4.35,4.35,4.26,4.17,4,3.86,3.66,3.35,3.05,2.67,2.27,1.83,1.44,1.17,0.92,0.69])


m, b = np.polyfit(x, y, 1)



print("a1=", m.round(6))
print("a0=", b.round(6))

plt.scatter(x,y)
plt.plot(x,y,'g', alpha=0.8)
plt.grid()
plt.show()