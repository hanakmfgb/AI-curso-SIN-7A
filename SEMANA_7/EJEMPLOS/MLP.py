# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 22:18:16 2025

@author: MARCELOFGB
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc

# 1. Carga y Preparación de Datos
# =====================================================================
# Cargar el dataset
data = pd.read_csv('diabetes.csv')

# Visualización inicial (opcional)
print(data.head())
print(data.describe())

# Separar características (X) y variable objetivo (y)
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Dividir en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Escalado de características (importante para redes neuronales)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 2. Creación y Entrenamiento del Modelo MLP
# =====================================================================
# Inicializar el modelo MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(2,15,17),  # Número de neuronas en cada capa oculta
                    activation='relu',       # Función de activación
                    solver='adam',           # Optimizador
                    max_iter=200,            # Número máximo de iteraciones
                    random_state=42)        # Semilla para reproducibilidad

# Entrenar el modelo
mlp.fit(X_train, y_train)

# 3. Evaluación del Modelo
# =====================================================================
# Predicciones en el conjunto de prueba
y_pred = mlp.predict(X_test)

# Matriz de Confusión
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Matriz de Confusión')
plt.show()

# Reporte de Clasificación
print(classification_report(y_test, y_pred))

# Curva ROC y AUC
y_pred_proba = mlp.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'AUC = {roc_auc:.2f}')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('Tasa de Falsos Positivos')
plt.ylabel('Tasa de Verdaderos Positivos')
plt.title('Curva ROC')
plt.legend(loc='lower right')
plt.show()

# 4. Análisis Adicional (Opcional)
# =====================================================================
# Visualización de la pérdida durante el entrenamiento
plt.figure(figsize=(8, 6))
plt.plot(mlp.loss_curve_)
plt.xlabel('Iteración')
plt.ylabel('Pérdida')
plt.title('Pérdida durante el Entrenamiento')
plt.show()

# Importancia de las características (aproximada, no siempre fiable en MLP)
# Esto requiere un poco más de trabajo e interpretación
# Una forma sencilla es observar las magnitudes de los pesos de la primera capa

if hasattr(mlp, 'coefs_'):
    plt.figure(figsize=(10, 6))
    plt.bar(X.columns, np.abs(mlp.coefs_[0]).mean(axis=1)) #promedio de los valores absolutos de los pesos
    plt.xlabel('Característica')
    plt.ylabel('Importancia (aproximada)')
    plt.title('Importancia Aprox. de las Características (Basada en Pesos)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
else:
    print("El modelo no proporciona acceso directo a los coeficientes para la importancia de las características.")