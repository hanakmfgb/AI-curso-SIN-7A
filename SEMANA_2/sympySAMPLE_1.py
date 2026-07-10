# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 21:24:12 2025

@author: MARCELOFGB
"""

import sympy
import numpy as np
import matplotlib.pyplot as plt

# 1. Definir el símbolo (la variable)
x = sympy.symbols('x')

# 2. Definir la ecuación
ecuacion = x**2 - 4   # Ejemplo: x^2 - 4 = 0

# 3. Resolver la ecuación
soluciones = sympy.solve(ecuacion, x)

print("Soluciones algebraicas de la ecuación:", soluciones)

# 4. Convertir la expresión simbólica en una función numérica (para graficar)
# Necesitamos una función que tome un valor numérico de 'x' y devuelva el resultado
f = sympy.lambdify(x, ecuacion, "numpy")  # 'numpy' para compatibilidad con NumPy

# 5. Crear datos para la gráfica
x_vals = np.linspace(-5, 5, 100)  # 100 puntos entre -5 y 5
y_vals = f(x_vals)  # Calcular los valores de 'y' (el resultado de la ecuación)

# 6. Crear la gráfica
plt.figure(figsize=(8, 6))  # Tamaño de la figura
plt.plot(x_vals, y_vals, label=str(ecuacion))  # Graficar la función
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de la ecuación')
plt.grid(True)  # Agregar una grilla
plt.legend()  # Mostrar la leyenda

# Marcar las raíces (soluciones) en la gráfica
#for sol in soluciones:
 #   plt.plot(sol, 0, 'ro', markersize=8, label=f'Raíz: {sol}')  # 'ro' es rojo y 'o' para círculo
    
    
    # --- CORRECCIÓN AQUÍ ---
# Marcar SOLO las raíces REALES en la gráfica
for sol in soluciones:
    # Preguntamos si la solución es un número real
    if sol.is_real:
        # Convertimos el valor simbólico a float (decimal) para matplotlib
        val_numerico = float(sol)
        plt.plot(val_numerico, 0, 'ro', markersize=8, label=f'Raíz Real: {val_numerico:.2f}')
    else:
        print(f"Nota: Se ignoró la raíz compleja {sol.evalf()} para la gráfica.")


plt.legend() #Para que se muestre la leyenda de las raices, después de haberlas graficado

plt.show()  # Mostrar la gráfica