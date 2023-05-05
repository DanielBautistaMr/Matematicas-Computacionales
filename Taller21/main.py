import numpy as np

x1 = np.array([1, 1, 2, 3, 1, 2, 3, 3])
x2 = np.array([0, 1, 1, 2, 2, 3, 3, 1])
y = np.array([3.2, 6, 2.2, 2.5, 6.5, 6.6, 3.5, 0.2])

X = np.column_stack((np.ones(len(x1)), x1, x2))
beta_hat = np.linalg.lstsq(X, y, rcond=None)[0]
r = np.corrcoef(np.column_stack((x1, x2, y)).T)[0,2]

print("Coeficientes de la función lineal:")
print(beta_hat)
print("Coeficiente de correlación (r):", r)