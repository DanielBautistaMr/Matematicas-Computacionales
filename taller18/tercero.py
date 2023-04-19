import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
y = np.array([4.2,6.5,7.5,8,8.5,8.8,9,9.1])


A = np.vstack([x, np.ones(len(x))]).T
beta, log_alpha = np.linalg.lstsq(A, np.log(y), rcond = None)[0]
alpha = np.exp(log_alpha)
print(f'alpha={alpha}, beta={beta}')

plt.figure(figsize = (10,10))
plt.plot(x, y, 'b.')
plt.plot(x, alpha*np.exp(beta*x), 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()