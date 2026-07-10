# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 20:38:42 2025

@author: MARCELOFGB
"""

import torch
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Ejemplo 1: Tensores en PyTorch

# Creación de tensores
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])

# Imprimir los tensores
print("Tensor a:", a)
print("Tensor b:", b)

# Operaciones básicas con tensores
suma = a + b
producto = a * b

# Imprimir los resultados
print("Suma:", suma)
print("Producto:", producto)

# Convertir tensores a NumPy para graficar
a_np = a.numpy()
b_np = b.numpy()
suma_np = suma.numpy()

# Gráfica simple
plt.plot(a_np, label='Tensor a')
plt.plot(b_np, label='Tensor b')
plt.plot(suma_np, label='Suma (a+b)')
plt.legend()
plt.title("Operaciones con Tensores en PyTorch")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.grid(True)
plt.show()