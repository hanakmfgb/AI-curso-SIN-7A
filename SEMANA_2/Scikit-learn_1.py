# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 19:25:00 2025

@author: MARCELOFGB
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Cargar el dataset desde el archivo CSV

df = pd.read_csv("Air_Quality.csv")

# Convertir 'Data Value' a numérico (si es posible)
df['Data Value'] = pd.to_numeric(df['Data Value'], errors='coerce')
df = df.dropna(subset=['Data Value']) # Eliminar filas con valores no numéricos
df = df.dropna(subset=['Geo Join ID']) # Eliminar filas con valores no numéricos
df['Geo Join ID'] = df['Geo Join ID'].astype(int)

# Seleccionar las características (X) y la variable objetivo (y)
X = df[['Geo Join ID']]  # Usamos 'Geo Join ID' como ejemplo de característica
y = df['Data Value']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo
model.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Visualizar los resultados
plt.scatter(X_test, y_test, color='blue', label='Datos reales')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicciones')
plt.xlabel('Geo Join ID')
plt.ylabel('Data Value')
plt.title('Regresión Lineal con Scikit-learn')
plt.legend()
plt.show()