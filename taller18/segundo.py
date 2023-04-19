import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x = np.array([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
y = np.array([4.2,6.5,7.5,8,8.5,8.8,9,9.1])


def exp_func(x, a, b):
    return a * np.exp(b * x)

params, cov = curve_fit(exp_func, x, y)


y_est = exp_func(x, params[0], params[1])

a, b = params

plt.scatter(x, y)
plt.plot(x, y_est, 'r-')
plt.title('Regresión exponencial')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

print(f"La función exponencial ajustada es: y = {a:.2f} * e^({b:.2f}x)")