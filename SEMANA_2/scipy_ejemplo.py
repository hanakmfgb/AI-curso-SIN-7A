# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 23:27:45 2025

@author: MARCELOFGB
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize,integrate,linalg,signal,stats

# 1. Optimización (scipy.optimize)
# Encontrar el mínimo de una función.

def funcion_a_minimizar(x):
    """Función simple para demostrar la optimización."""
    return x**2 - 4*x + 3

# Optimización sin restricciones usando el método de Nelder-Mead
resultado_optimizacion = optimize.minimize(funcion_a_minimizar, x0=0)  # x0 es el punto de partida

print("\n--- Optimización ---")
print("Resultado de la optimización:", resultado_optimizacion)  # Muestra el resultado completo
print("Mínimo encontrado:", resultado_optimizacion.x[0]) # Muestra solo el valor de x en el mínimo
print("Valor de la función en el mínimo:", funcion_a_minimizar(resultado_optimizacion.x[0]))

# 2. Integración Numérica (scipy.integrate)
# Calcular la integral definida de una función.

def funcion_a_integrar(x):
    """Función simple para demostrar la integración."""
    return x**2

# Integración usando quad (cuadratura)
resultado_integracion, error_estimado = integrate.quad(funcion_a_integrar, 0, 2) # Integra de 0 a 2

print("\n--- Integración Numérica ---")
print("Resultado de la integración:", resultado_integracion)
print("Error estimado:", error_estimado)

# 3. Álgebra Lineal (scipy.linalg)
# Resolver un sistema de ecuaciones lineales y calcular autovalores.

A = np.array([[2, 1], [1, 3]])  # Matriz de coeficientes
b = np.array([5, 8])  # Vector de términos independientes

# Resolver el sistema Ax = b
x = linalg.solve(A, b)

# Calcular los autovalores y autovectores de A
autovalores, autovectores = linalg.eig(A)

print("\n--- Álgebra Lineal ---")
print("Solución del sistema Ax=b:", x)
print("Autovalores de A:", autovalores)
print("Autovectores de A:\n", autovectores)

# 4. Procesamiento de Señales (scipy.signal)
# Generar una señal y aplicar un filtro.

# Generar una señal senoidal con ruido
tiempo = np.linspace(0, 1, 500, endpoint=False)
senal = np.sin(2*np.pi*5*tiempo) + 0.5*np.random.randn(500)  # 5 Hz con ruido

# Aplicar un filtro de media móvil
ventana = signal.windows.hann(50) # Usar una ventana de Hanning
senal_filtrada = signal.convolve(senal, ventana, mode='same') / sum(ventana) # Normalizar

print("\n--- Procesamiento de Señales ---")
# No imprimimos valores largos de la señal.
print("Señal original (ejemplo):\n", senal[:5]) # Mostramos los primeros 5 valores
print("Señal filtrada (ejemplo):\n", senal_filtrada[:5]) # Mostramos los primeros 5 valores

# 5. Estadística (scipy.stats)
# Generar números aleatorios de una distribución y realizar una prueba estadística.

# Generar números aleatorios de una distribución normal
datos_normales = stats.norm.rvs(loc=0, scale=1, size=100)  # Media 0, Desviación estándar 1

# Realizar una prueba t de una muestra para determinar si la media es diferente de 0.
resultado_ttest = stats.ttest_1samp(datos_normales, 0)

print("\n--- Estadística ---")
print("Prueba t de una muestra:", resultado_ttest) # Imprime el estadístico t y el valor p

# 6. Graficado (Usando Matplotlib para visualizar resultados)
# Graficamos la señal original y la señal filtrada.

plt.figure(figsize=(12, 6))

# Gráfico de la optimización
plt.subplot(2, 2, 1)  # 2 filas, 2 columnas, gráfico 1
x_vals = np.linspace(-2, 6, 100)
y_vals = funcion_a_minimizar(x_vals)
plt.plot(x_vals, y_vals, label='Función a Minimizar')
plt.scatter(resultado_optimizacion.x[0], funcion_a_minimizar(resultado_optimizacion.x[0]), color='red', label='Mínimo Encontrado')
plt.title('Optimización')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)

# Gráfico de la señal original y filtrada
plt.subplot(2, 2, 2)  # 2 filas, 2 columnas, gráfico 2
plt.plot(tiempo, senal, label='Señal Original')
plt.plot(tiempo, senal_filtrada, label='Señal Filtrada')
plt.title('Procesamiento de Señales')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)

#Histograma de la distribución normal
plt.subplot(2,2,3)
plt.hist(datos_normales, bins=20, density=True, alpha=0.6, color='g', label='Datos Normales')
plt.title("Distribución Normal")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.legend()
plt.grid(True)

plt.tight_layout()  # Ajusta los subtítulos para que no se superpongan
plt.show()