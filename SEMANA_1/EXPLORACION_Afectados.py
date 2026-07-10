# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 19:36:28 2024

@author: MARCELOFGB
"""

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Cargar el conjunto de datos de incidencias de mantenimiento
mant_data = pd.read_csv('C:/DATOS_EJEMPLO/INCIDENCIAS_DATA_CLI_ALL_MODELO.csv', delimiter=';')

###########################################################################################
#
# tipoincidencia;corte;planeado;anio;mes;semana;dia;hora;causa;subcausa;subestacion;tipodispositivo;afectados
#
###########################################################################################

#mant_data= mant_data[mant_data.anio == 2021]

# Ver las primeras filas del conjunto de datos
print("las primeras filas del conjunto de datos:")
print(mant_data.head())

# Estadísticas descriptivas
print("Estadísticas descriptivas:")
print(mant_data.describe())

# Dimensiones del dataset
print("Dimensiones del dataset:")
print(mant_data.shape)

# Número de datos ausentes por variable
print("Número de datos ausentes por variable:")
print(mant_data.isna().sum().sort_values())




plt.figure(figsize=(10, 6))
plt.xticks(np.arange(2017, 2023, 1.0))
sns.histplot(mant_data['anio'].dropna(), edgecolor = "white",linewidth = 2, 
             bins=6, kde=True, line_kws = {'linestyle':'dashed','linewidth':'2'}).lines[0].set_color('red')
plt.xlabel('Año')
plt.ylabel('Registros')
plt.title('Distribución de registros por año')
plt.show()


plt.figure(figsize=(10, 6))
plt.xticks(np.arange(1, 13, 1.0))
sns.histplot(mant_data['mes'].dropna(), edgecolor = "white",linewidth = 2, 
             bins=12, kde=True, line_kws = {'linestyle':'dashed','linewidth':'2'}).lines[0].set_color('red')
plt.xlabel('Mes')
plt.ylabel('Registros')
plt.title('Distribución de registros por mes')
plt.show()

plt.figure(figsize=(20, 6))
plt.xticks(np.arange(1, 54, 1.0))
sns.histplot(mant_data['semana'].dropna(), edgecolor = "white",linewidth = 2, 
             bins=53, kde=True, line_kws = {'linestyle':'dashed','linewidth':'2'}).lines[0].set_color('red')
plt.xlabel('Semana')
plt.ylabel('Registros')
plt.title('Distribución de registros por semana')
plt.show()

plt.figure(figsize=(10, 6))
plt.xticks(np.arange(1, 8, 1.0))
sns.histplot(mant_data['dia'].dropna(), edgecolor = "white",linewidth = 2, 
             bins=7, kde=True, line_kws = {'linestyle':'dashed','linewidth':'2'}).lines[0].set_color('red')
plt.xlabel('Día')
plt.ylabel('Registros')
plt.title('Distribución de registros por día')
plt.show()


plt.figure(figsize=(10, 6))
plt.xticks(np.arange(0, 24, 1.0))
sns.histplot(mant_data['hora'].dropna(), edgecolor = "white",linewidth = 2, 
             bins=23, kde=True, line_kws = {'linestyle':'dashed','linewidth':'2'}).lines[0].set_color('red')
plt.xlabel('Hora')
plt.ylabel('Registros')
plt.title('Distribución de registros por hora')
plt.show()

plt.figure(figsize=(20, 6))
plt.xticks(np.arange(1, 17, 1.0))
sns.histplot(mant_data['causa'].dropna(), edgecolor = "white",linewidth = 2, 
             bins=16, kde=True, line_kws = {'linestyle':'dashed','linewidth':'2'}).lines[0].set_color('red')
plt.xlabel('Causa')
plt.ylabel('Registros')
plt.title('Distribución de registros por causa')
plt.show()

plt.figure(figsize=(15, 6))
plt.xticks(np.arange(1, 47, 1.0))
sns.histplot(mant_data['subcausa'].dropna(), edgecolor = "white",linewidth = 2, 
             bins=46, kde=True, line_kws = {'linestyle':'dashed','linewidth':'2'}).lines[0].set_color('red')
plt.xlabel('Subcausa')
plt.ylabel('Registros')
plt.title('Distribución de registros por subcausa')
plt.show()

plt.figure(figsize=(10, 6))
plt.xticks(np.arange(1, 29, 1.0))
sns.histplot(mant_data['subestacion'].dropna(), edgecolor = "white",linewidth = 2, 
             bins=28, kde=True, line_kws = {'linestyle':'dashed','linewidth':'2'}).lines[0].set_color('red')
plt.xlabel('Subestacion')
plt.ylabel('Registros')
plt.title('Distribución de registros por subestacion')
plt.show()



#MATRIZ DE CORRELACION
variables_numericas = [ 
#'tipoincidencia'
#,'corte'
#,'planeado'
'anio'
,'mes'
,'semana'
,'dia'
,'hora'
,'causa'
,'subcausa'
,'subestacion'
#,'tipodispositivo'
,'afectados']
# Crear una submatriz de correlación
correlation_matrix = mant_data[variables_numericas].corr()
# Crear un mapa de calor de correlación
plt.figure(figsize=(15, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Matriz de Correlación entre Variables Numéricas')
plt.show()


