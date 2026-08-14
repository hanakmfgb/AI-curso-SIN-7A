# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 22:11:08 2025

@author: MARCELOFGB
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
data = pd.read_csv('diabetes.csv')

# Mostrar las primeras filas para entender la estructura
print(data.head())

# Separar características (X) y variable objetivo (y)
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar el modelo
tree = DecisionTreeClassifier(max_depth=200) # Puedes ajustar la profundidad máxima
#, min_samples_split=9, min_samples_leaf=9, max_features='log2', class_weight='balanced')  

# Entrenar el modelo
tree.fit(X_train, y_train)

plt.figure(figsize=(20,10))
plot_tree(tree, feature_names=X.columns, class_names=['No Diabetes', 'Diabetes'], filled=True)
plt.show()

# Predecir sobre el conjunto de prueba
y_pred = tree.predict(X_test)

# Calcular la precisión
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión: {accuracy:.2f}")

# Generar el reporte de clasificación
print("\nReporte de Clasificación:")
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['No Diabetes', 'Diabetes'], 
            yticklabels=['No Diabetes', 'Diabetes'])
plt.xlabel('Predicciones')
plt.ylabel('Valores Reales')
plt.title('Matriz de Confusión')
plt.show()