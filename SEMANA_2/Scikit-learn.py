# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 21:50:44 2025

@author: MARCELOFGB
"""
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Cargar los datos desde la cadena de texto directamente (sin guardar el archivo)
df = pd.read_csv('Air_Quality.csv',index_col='Unique ID')


# Filtrar los datos para el indicador de partículas finas (PM 2.5)
pm25_df = df[(df['Name'] == 'Fine particles (PM 2.5)') & (df['Measure'] == 'Mean')]

# Imprimir información sobre el DataFrame filtrado
print("\nDataFrame de Partículas Finas (PM 2.5):\n", pm25_df.head())
print("\nInformación del DataFrame de Partículas Finas (PM 2.5):\n", pm25_df.info())

# Convertir 'Data Value' a numérico y eliminar filas con valores NaN
pm25_df['Data Value'] = pd.to_numeric(pm25_df['Data Value'], errors='coerce')
pm25_df = pm25_df.dropna(subset=['Data Value'])

# Crear la variable 'Year' a partir de 'Time Period'
def extract_year(time_period):
    try:
        if 'Annual Average' in time_period:
            return int(time_period.split(' ')[2])
        elif 'Summer' in time_period or 'Winter' in time_period:
            return int(time_period.split(' ')[1])
        else:
            return int(time_period)
    except:
        return None

pm25_df['Year'] = pm25_df['Time Period'].apply(extract_year)

# Eliminar filas donde 'Year' es NaN después de la extracción
pm25_df = pm25_df.dropna(subset=['Year'])
pm25_df['Year'] = pm25_df['Year'].astype(int)

# Preparar datos para el modelo
X = pm25_df[['Year']]  # Característica: Año
y = pm25_df['Data Value']  # Variable objetivo: Valor de PM2.5

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Realizar predicciones
y_pred = model.predict(X_test)

# Visualizar los resultados
plt.scatter(X_test, y_test, color='black', label='Datos Reales')
plt.plot(X_test, y_pred, color='blue', linewidth=3, label='Regresión Lineal')
plt.xlabel('Año')
plt.ylabel('Nivel de PM2.5 (mcg/m3)')
plt.title('Regresión Lineal del Nivel de PM2.5 a lo largo del Tiempo')
plt.legend()
plt.show()

print("Predicciones:\n", y_pred)