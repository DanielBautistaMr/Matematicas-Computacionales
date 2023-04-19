import numpy as np
import matplotlib.pyplot as plt

xn=np.array([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5])

yn=np.array([4.2, 6.5, 7.5, 8, 8.5, 8.8, 9, 9.1])

n=len(xn)

Sum_x=sum(xn)
Sum_y=sum(yn)
Sum_xx=sum(xn**2)
Sum_xy=sum(xn*yn)

print(Sum_x, Sum_y, Sum_xx, Sum_xy)

a_0=(Sum_xx*Sum_y-Sum_xy*Sum_x)/(n*Sum_xx-Sum_x**2)
a_1=(n*Sum_xy-Sum_x*Sum_y)/(n*Sum_xx-Sum_x**2)
print(a_0, a_1)

x=np.linspace(0, 9)
y=a_0+a_1*x

plt.figure(1)

plt.scatter(xn, yn, color='b')
plt.grid(linestyle='dotted')
plt.plot(x, y, color='r')

plt.title(r'Regresión por Mínimos', fontsize=10)
plt.xlabel(r'x', fontsize=10)
plt.ylabel(r'y', fontsize=10)

plt.show()