# -*- coding: utf-8 -*-
"""
Created on Sat May 18 22:52:12 2024

@author: MARCELOFGB
"""
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from scipy.stats import stats
#from fitter import Fitter#,get_common_distributions
from distfit import distfit
import matplotlib.ticker as ticker

# Cargar el conjunto de datos de afectados de mantenimiento
data_U1 = pd.read_csv('C:/DATOS_EJEMPLO/INCIDENCIAS_DATA_CLI_ALL_MODELO.csv', delimiter=';')

#tipoincidencia;corte;planeado;anio;mes;semana;causa;subcausa;subestacion;tipodispositivo;afectados


# Ver las primeras filas del conjunto de datos
print(data_U1.head())

# Tipo de datos
print(data_U1.info())


# Dimensiones del dataset
print(data_U1.shape)

# Número de datos ausentes por variable
print(data_U1.isna().sum().sort_values())

# Estadísticas de variables categóricas
#print(mant_data.describe(include=['object']))

#data_U1= mant_data[(mant_data.INCIDENCIAS >0)]
#data_U1= mant_data

print(data_U1.info())

fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(12, 8))

sns.kdeplot(
    data_U1.afectados,
    fill    = True,
    color   = "blue",
    ax      = axes[0]
)
sns.rugplot(
    data_U1.afectados,
    color   = "blue",
    ax      = axes[0]
)
axes[0].set_title("Distribución original", fontsize = 'medium')
axes[0].set_xlabel('afectados', fontsize='medium') 
axes[0].tick_params(labelsize = 7)

sns.kdeplot(
    np.sqrt(data_U1.afectados),
    fill    = True,
    color   = "blue",
    ax      = axes[1]
)
sns.rugplot(
    np.sqrt(data_U1.afectados),
    color   = "blue",
    ax      = axes[1]
)
axes[1].set_title("Transformación raíz cuadrada", fontsize = 'medium')
axes[1].set_xlabel('sqrt(afectados)', fontsize='medium') 
axes[1].tick_params(labelsize = 7)

sns.kdeplot(
    np.log(data_U1.afectados),
    fill    = True,
    color   = "blue",
    ax      = axes[2]
)
sns.rugplot(
    np.log(data_U1.afectados),
    color   = "blue",
    ax      = axes[2]
)
axes[2].set_title("Transformación logarítmica", fontsize = 'medium')
axes[2].set_xlabel('log(afectados)', fontsize='medium') 
axes[2].tick_params(labelsize = 7)

fig.tight_layout()



# Initialize distfit
dist = distfit(distr='full')

# Determine best-fitting probability distribution for data
dist.fit_transform(data_U1.afectados)
print(dist.summary)
best_distr = dist.model
print(best_distr)

dist.plot()

# Explorar las columnas del DataFrame
#print(data_U1.columns)

# Seleccionar las dos columnas que quieres graficar
# Ajusta 'columna_x' y 'columna_y' con los nombres reales de tus columnas

columna_x = 'dia'
columna_y = 'afectados'

# Crear el gráfico de dispersión
plt.figure(figsize=(10, 6))  # Ajusta el tamaño del gráfico si es necesario
plt.scatter(data_U1[columna_x], data_U1[columna_y])
plt.xlabel(columna_x)
plt.ylabel(columna_y)
plt.title('Gráfico de Dispersión de ' + columna_x + ' vs ' + columna_y)
plt.grid(True)
plt.show()

columna_x = 'hora'
columna_y = 'afectados'

# Crear el gráfico de dispersión
plt.figure(figsize=(10, 6))  # Ajusta el tamaño del gráfico si es necesario
plt.scatter(data_U1[columna_x], data_U1[columna_y])
plt.xlabel(columna_x)
plt.ylabel(columna_y)
plt.title('Gráfico de Dispersión de ' + columna_x + ' vs ' + columna_y + ' (Breaker)')
plt.grid(True)
plt.show()


# Seleccionar las dos columnas que quieres graficar
# Ajusta 'columna_x' y 'columna_y' con los nombres reales de tus columnas

columna_x = 'tipodispositivo'
columna_y = 'afectados'

# Crear el gráfico de dispersión
plt.figure(figsize=(10, 6))  # Ajusta el tamaño del gráfico si es necesario
plt.scatter(data_U1[columna_x], data_U1[columna_y])
plt.xlabel(columna_x)
plt.ylabel(columna_y)
plt.title('Gráfico de Dispersión de ' + columna_x + ' vs ' + columna_y)
plt.grid(True)
plt.show()


# Variables numéricas
# ==============================================================================
#print(data_U1.select_dtypes(include=['int']).describe())


#distribuciones = ['beta']#'gamma', 'rayleigh', 'uniform',"cauchy","chi2", "expon", "exponpow", "gamma",   "norm", "powerlaw", "beta", "logistic"]
#f = Fitter(data_U1.afectados, distributions=distribuciones)
#f.fit()
#f.summary( plot=False)#Nbest=10
#distribución BETA variabilidad sobre un rango fijo, incertidumbre en la probabilidad de ocurrencia de un evento.
#f = Fitter(data_U1.afectados, distributions= ['beta'])
#f.fit()
#f.summary(plot=False)
#f.hist()
#plt.show 


# Gráfico de distribución para cada variable numérica
# ==============================================================================
# Ajustar número de subplots en función del número de columnas
fig, axes = plt.subplots(nrows=9, ncols=1, figsize=(12, 12))
axes = axes.flat
columnas_numeric = data_U1.select_dtypes(include=['float64','int']).columns
#columnas_numeric = columnas_numeric.drop('tipoincidencia')
#columnas_numeric = columnas_numeric.drop('corte')
#columnas_numeric = columnas_numeric.drop('planeado')
#columnas_numeric = columnas_numeric.drop('anio')
#columnas_numeric = columnas_numeric.drop('mes')
#columnas_numeric = columnas_numeric.drop('semana')
#columnas_numeric = columnas_numeric.drop('tipodispositivo')
columnas_numeric = columnas_numeric.drop('afectados')
#print(str(columnas_numeric))
#tipoincidencia;corte;planeado;anio;mes;semana;causa;subcausa;subestacion;tipodispositivo;afectados
#anio;mes;semana;causa;subcausa;subestacion;tipodispositivo
#anio,mes,semana,dia,hora,subestacion,causa,subcausa,tipodispositivo,afectados

col=0
for i, colum in enumerate(columnas_numeric):
    if i == 0:  # True
        plt.xticks(np.arange(2017, 2023, 1))        
        col=6
    if i == 1:  # True
        plt.xticks(np.arange(1, 13, 1))
        col=12
    if i == 2:  # True
        plt.xticks(np.arange(1, 54, 1))
        col=53
    if i == 3:  # True
        plt.xticks(np.arange(1, 8, 1))
        col=7
    if i == 4:  # True
        plt.xticks(np.arange(0, 24,1))
        col=23
    if i == 5:  # True
        plt.xticks(np.arange(1, 29, 1))
        col=28
    if i == 6:  # True
        plt.xticks(np.arange(1, 17, 1))
        col=16
    if i == 7:  # True
        plt.xticks(np.arange(1, 47, 1))
        col=46            
    if i == 8:  # True
        plt.xticks(np.arange(1, 34, 1))
        col=33
    sns.histplot(
        data     = data_U1,
        x        = colum,
        stat     = "count",
        bins     = col,
        kde      = True,
        color    = (list(plt.rcParams['axes.prop_cycle'])*2)[i]["color"],
        line_kws = {'linewidth': 2},
        alpha    = 0.3,
        ax       = axes[i]
    )
        
    axes[i].set_title(colum, fontsize = 10, fontweight = "bold")
    axes[i].tick_params(labelsize = 10)
    axes[i].set_xlabel("")
    
    if i == 0:  # True
        axes[i].set_xticks(range(2017,2023))
    if i == 1:  # True
        axes[i].set_xticks(range(1,13))
    if i == 2:  # True
        axes[i].set_xticks(range(1,54))
    if i == 3:  # True
        axes[i].set_xticks(range(1,8))
    if i == 4:  # True
        axes[i].set_xticks(range(0,24))
    if i == 5:  # True
        axes[i].set_xticks(range(1,29))
    if i == 6:  # True
        axes[i].set_xticks(range(1,17))
    if i == 7:  # True
        axes[i].set_xticks(range(1,47))
    if i == 8:  # True
        axes[i].set_xticks(range(1,34))
# Se eliminan los axes vacíos
#for i in [6]:
#fig.delaxes(axes[7])
        
fig.tight_layout()
plt.subplots_adjust(top = 0.9)
fig.suptitle('Distribución variables numéricas (INCIDENCIAS REPORTADAS)', fontsize = 12, fontweight = "bold");


# Gráfico de distribución para cada variable numérica
# ==============================================================================
# Ajustar número de subplots en función del número de columnas
fig, axes = plt.subplots(nrows=9, ncols=1, figsize=(12, 12))
axes = axes.flat
columnas_numeric = data_U1.select_dtypes(include=['float64','int']).columns
#columnas_numeric = columnas_numeric.drop('tipoincidencia')
#columnas_numeric = columnas_numeric.drop('corte')
#columnas_numeric = columnas_numeric.drop('planeado')
#columnas_numeric = columnas_numeric.drop('semana')
#olumnas_numeric = columnas_numeric.drop('mes')
#columnas_numeric = columnas_numeric.drop('anio')
columnas_numeric = columnas_numeric.drop('afectados')
#columnas_numeric = columnas_numeric.drop('tipodispositivo')


for i, colum in enumerate(columnas_numeric):
    sns.regplot(
        x           = data_U1[colum],
        y           = data_U1['afectados'],
        color       = "gray",
        marker      = '.',
        scatter_kws = {"alpha":0.4},
        line_kws    = {"color":"r","alpha":0.7},
        ax          = axes[i]
    )
    axes[i].set_title(f"afectados vs {colum}", fontsize = 12, fontweight = "bold")
    #axes[i].ticklabel_format(style='sci', scilimits=(-4,4), axis='both')
    axes[i].yaxis.set_major_formatter(ticker.EngFormatter())
    axes[i].xaxis.set_major_formatter(ticker.EngFormatter())
    axes[i].tick_params(labelsize = 10)
    axes[i].set_xlabel("")
    axes[i].set_ylabel("")
    
    if i == 0:  # True
        axes[i].set_xticks(range(2017,2023))
    if i == 1:  # True
        axes[i].set_xticks(range(1,13))
    if i == 2:  # True
        axes[i].set_xticks(range(1,54))
    if i == 3:  # True
        axes[i].set_xticks(range(1,8))
    if i == 4:  # True
        axes[i].set_xticks(range(0,24))
    if i == 5:  # True
        axes[i].set_xticks(range(1,29))
    if i == 6:  # True
        axes[i].set_xticks(range(1,17))
    if i == 7:  # True
        axes[i].set_xticks(range(1,47))        
    if i == 8:  # True
        axes[i].set_xticks(range(1,34))
# Se eliminan los axes vacíos
#fig.delaxes(axes[7])
    
fig.tight_layout()
plt.subplots_adjust(top=0.9)
fig.suptitle('Correlación con afectados', fontsize = 12, fontweight = "bold");



#MATRIZ DE CORRELACION

#corte;planeado;semana;mes;anio;causa;subcausa;subtipo;subestacion;tipodispositivo;afectados
# Seleccionar las variables numéricas principales para el análisis de correlación
#tipoincidencia;corte;planeado;anio;mes;semana;causa;subcausa;subestacion;tipodispositivo;afectados
#anio,mes,semana,dia,hora,subestacion,causa,subcausa,tipodispositivo,afectados
variables_numericas = ['anio','mes','semana','dia','hora','subestacion','causa','subcausa','tipodispositivo','afectados']

#Crear una submatriz de correlación
correlation_matrix = data_U1[variables_numericas].corr()


# Crear un mapa de calor de correlación


# Correlación entre columnas numéricas
# ==============================================================================
def tidy_corr_matrix(corr_mat):
    
    #Función para convertir una matrix de correlación de pandas en formato tidy
    
    corr_mat = corr_mat.stack().reset_index()
    corr_mat.columns = ['variable_1','variable_2','r']
    corr_mat = corr_mat.loc[corr_mat['variable_1'] != corr_mat['variable_2'], :]
    corr_mat['abs_r'] = np.abs(corr_mat['r'])
    corr_mat = corr_mat.sort_values('abs_r', ascending=False)
    
    return(corr_mat)

correlation_matrix = data_U1[variables_numericas].corr(method='pearson')
print(tidy_corr_matrix(correlation_matrix).head(10))

# Heatmap matriz de correlaciones
# ==============================================================================
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 9))
plt.title('Matriz de Correlación entre Variables Numéricas',fontsize = 12, fontweight = "bold")
sns.heatmap(
    correlation_matrix,
    annot     = True,
    cbar      = False,
    annot_kws = {"size": 11},
    vmin      = -1,
    vmax      = 1,
    center    = 0,
    cmap      = sns.diverging_palette(20, 220, n=200),
    square    = True,
    ax        = ax
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation = 45,
    horizontalalignment = 'right',
)

ax.tick_params(labelsize = 12)

#plt.figure(figsize=(12, 9))
#sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
#plt.title('Matriz de Correlación entre Variables Numéricas')
#plt.show()


# Gráfico relación 
# ==============================================================================
# Ajustar número de subplots en función del número de columnas
plt.figure(figsize=(25, 10))
plt.title('Distribución de afectados por hora', fontsize = 12, fontweight = "bold");
#fig = plt.subplots(nrows=1, ncols=1, figsize=(10, 5))
#axes = axes.flat
#columnas_object = data_U1.columns
sns.violinplot(
        x     = 'hora',
        y     = 'afectados',
        data  = data_U1,
        color = "blue"#,
        #ax    = plt
    )
plt.tick_params(labelsize = 12)
