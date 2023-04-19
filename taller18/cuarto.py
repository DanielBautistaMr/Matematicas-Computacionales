import numpy as np
import matplotlib.pyplot as plt

xn=np.array([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5])

yn=np.array([4.2, 6.5, 7.5, 8, 8.5, 8.8, 9, 9.1])

ly=1/yn
lx=1/xn

n=len(xn)

Sum_x=sum(lx)
Sum_y=sum(ly)
Sum_xx=sum(lx**2)
Sum_xy=sum(lx*ly)

print(Sum_x, Sum_y, Sum_xx, Sum_xy)

a_1 =(n*Sum_xy-Sum_x*Sum_y)/(n*Sum_xx-Sum_x**2)
a_0 = (Sum_y/n)-(a_1*Sum_x/n)


α=1/a_0
β=a_1/a_0

print('alpha=', α)


x= np.linspace(0,9)
y=α*(x/(β+x))

plt.figure(1)

plt.scatter(xn,yn, color='r')
plt.grid(linestyle='dotted')
plt.plot(x,y, color='b')

plt.xlabel(r'x', fontsize=10)
plt.ylabel(r'y', fontsize=10)

plt.show()
