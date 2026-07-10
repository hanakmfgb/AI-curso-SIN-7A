# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 21:04:32 2025

@author: MARCELOFGB
"""
import torch
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Ejemplo 2: Aprendizaje Profundo con Dataset CSV

# Cargar el dataset 
df = pd.read_csv('Air_Quality.csv',index_col='Unique ID')  # Usar io.StringIO para leer desde una cadena

# Selección y preparación de datos (seleccionar dos columnas)
X = df[['Indicator ID', 'Geo Join ID']].values  # Características
y = df['Data Value'].values  # Variable objetivo

# Manejar NaN (rellenar con la media)
X = np.nan_to_num(X, nan=np.nanmean(X))
y = np.nan_to_num(y, nan=np.nanmean(y))

# Convertir a tensores
X_tensor = torch.tensor(X, dtype=torch.float32)
y_tensor = torch.tensor(y, dtype=torch.float32).reshape(-1, 1)  # Asegurar forma (n, 1)

# Definir una red neuronal sencilla
modelo = torch.nn.Sequential(
    torch.nn.Linear(2, 8),  # Capa de entrada (2 características) a 8 neuronas
    torch.nn.ReLU(),
    torch.nn.Linear(8, 1)   # Capa de salida (1 valor)
)

# Función de pérdida y optimizador
criterion = torch.nn.MSELoss()
optimizer = torch.optim.Adam(modelo.parameters(), lr=0.01)

# Entrenamiento del modelo
epochs = 1500  #Número de épocas
for epoch in range(epochs):
    # Predicción
    y_pred = modelo(X_tensor)
    # Cálculo de la pérdida
    loss = criterion(y_pred, y_tensor)
    # Backpropagation y optimización
    optimizer.zero_grad()  # Limpiar los gradientes anteriores
    loss.backward()        # Calcular los gradientes
    optimizer.step()       # Actualizar los pesos
    # Imprimir la pérdida cada 10 épocas
    if (epoch+1) % 10 == 0:
        print(f'Epoch: {epoch+1}, Loss: {loss.item():.4f}')

# Evaluar el modelo
modelo.eval() #poner en modo evaluacion
with torch.no_grad():
    predicted = modelo(X_tensor).numpy()

#Graficar resultados
plt.figure(figsize=(10,6))
plt.scatter(X[:, 0], y, label='Datos reales')
plt.scatter(X[:, 0], predicted, label='Predicciones', color='red', marker='x')
plt.xlabel('Indicator ID')
plt.ylabel('Data Value')
plt.title('Predicciones del modelo vs. Datos reales')
plt.legend()
plt.grid(True)
plt.show()