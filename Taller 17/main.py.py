# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nc-nSPUDmKWZASi586yr4KHEoRp-Isdp
"""

import numpy as np
import matplotlib.pyplot as plt

# Datos de entrada
xn = np.array([2, 4, 6, 8, 10, 12])
yn = np.array([2.2, 3, 4.5, 6, 8.5, 12])

# Cálculo de la regresión lineal
lny = np.log(yn)
a_1, a_0 = np.polyfit(xn, lny, 1)

# Cálculo del parámetro alpha
alpha = np.exp(a_0)

# Generación de la recta de regresión
x = np.linspace(0, 12,100)
y = alpha * np.exp(a_1*x)

# Gráfica
plt.figure()
plt.scatter(xn, yn, color='r')
plt.plot(x, y, color='b')
plt.grid(linestyle='dotted')
plt.title('Regresión por mínimos cuadrados', fontsize=10)
plt.xlabel('x', fontsize=10)
plt.ylabel('y', fontsize=10)
plt.show()