# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 18:23:14 2025

@author: MARCELOFGB
"""

import pandas as pd

# Cargar el archivo CSV en un DataFrame
try:
    df = pd.read_csv('Air_Quality.csv')
except FileNotFoundError:
    print("Error: No se encontró el archivo Air_Quality.csv. Asegúrate de que esté en el directorio correcto.")
    exit()

# Mostrar las primeras filas del DataFrame para verificar la carga
print("Primeras 5 filas del DataFrame:")
print(df.head())

# Ejemplo 1: Filtrar datos por nombre del contaminante (Ozone)
ozone_data = df[df['Name'] == 'Ozone (O3)']  # Filtra las filas donde la columna 'Name' es '386 Ozone (03)'
print("\nDatos de Ozone:")
print(ozone_data[['Geo Place Name', 'Time Period', 'Data Value']]) # Mostrar solo la información de algunas columnas.

# Ejemplo 2:  Extraer datos de PM2.5 con valor superior a 9 y mostrar lugar
pm25_high = df[(df['Name'] == 'Fine particles (PM 2.5)') & (df['Data Value'] >9)]
print("\nDatos de PM2.5 con valor superior a 9:")
print(pm25_high[['Geo Place Name', 'Time Period', 'Data Value']])

# Ejemplo 3: Calcular el promedio de 'Data Value' para cada 'Geo Place Name'
promedios_por_lugar = df.groupby('Geo Place Name')['Data Value'].mean()
print("\nPromedio de 'Data Value' por 'Geo Place Name':")
print(promedios_por_lugar)