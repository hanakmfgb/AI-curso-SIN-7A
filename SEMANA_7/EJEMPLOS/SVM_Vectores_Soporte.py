import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris # Dataset Iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC # Support Vector Classifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, # Métricas de clasificación
    roc_auc_score, roc_curve, # Para la Curva ROC (solo para problemas binarios)
    confusion_matrix, ConfusionMatrixDisplay # Para la Matriz de Confusión
)

# ==============================================================================
# 1. Carga del Dataset y Preparación de Datos (para clasificación binaria y 2D)
# ==============================================================================
# Cargamos el conjunto de datos de Iris.
iris = load_iris()
X_full = iris.data  # Características (sepal length, sepal width, petal length, petal width)
y_full = iris.target # Variable objetivo (0: setosa, 1: versicolor, 2: virginica)
feature_names_full = iris.feature_names
target_names_full = iris.target_names

print("--- Información del Dataset Original de Iris ---")
print(f"Número total de muestras: {X_full.shape[0]}")
print(f"Número total de características: {X_full.shape[1]}")
print(f"Nombres de las características: {feature_names_full}")
print(f"Clases disponibles: {target_names_full}\n")

# Para este ejemplo didáctico, seleccionaremos:
# - Solo dos características: 'petal length (cm)' y 'petal width (cm)' (columnas 2 y 3)
# - Solo dos clases: 'versicolor' (1) y 'virginica' (2). Excluiremos 'setosa' (0) ya que es linealmente separable.
# Esto nos permitirá visualizar la frontera de decisión en 2D.

# Seleccionar solo las muestras de versicolor (1) y virginica (2)
selected_indices = (y_full == 1) | (y_full == 2)
X = X_full[selected_indices]
y = y_full[selected_indices]

# Ajustar las etiquetas de clase a 0 y 1 para una clasificación binaria estándar
y[y == 1] = 0 # versicolor -> 0
y[y == 2] = 1 # virginica -> 1

# Seleccionar solo las características 2 y 3 (longitud y anchura del pétalo)
X = X[:, [2, 3]]
selected_feature_names = [feature_names_full[2], feature_names_full[3]]
selected_target_names = ['versicolor', 'virginica']

print("--- Dataset Reducido para el Ejemplo ---")
print(f"Número de muestras seleccionadas: {X.shape[0]}")
print(f"Número de características seleccionadas: {X.shape[1]}")
print(f"Características utilizadas: {selected_feature_names}")
print(f"Clases a predecir (0: {selected_target_names[0]}, 1: {selected_target_names[1]})\n")

# Dividimos el conjunto de datos en entrenamiento y prueba.
# split: 80% train / 20% test
# stratify=y para asegurar proporciones de clases balanceadas en ambos conjuntos.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y) # stratify para balance

print("--- Dimensiones de los conjuntos de datos ---")
print(f"Dimensiones de X_train (entrenamiento): {X_train.shape}")
print(f"Dimensiones de y_train (entrenamiento): {y_train.shape}")
print(f"Dimensiones de X_test (prueba): {X_test.shape}")
print(f"Dimensiones de y_test (prueba): {y_test.shape}\n")

# ==============================================================================
# 2. Construcción y Entrenamiento del Modelo de SVM (SVC)
# ==============================================================================
# Creamos una instancia del Support Vector Classifier (SVC).
# - kernel='rbf': Usamos el kernel RBF (Radial Basis Function) para manejar fronteras de decisión no lineales.
# - gamma=0.5: Parámetro para el kernel RBF. Controla la 'amplitud' de la influencia de cada punto.
# - C=1.0: Parámetro de regularización. Controla el balance entre un margen amplio y clasificar correctamente.
# - probability=True: Habilitamos la predicción de probabilidades para poder generar la curva ROC.
# - random_state=42: Para reproducibilidad.

model = SVC(kernel='rbf', gamma=0.6, C=1.0, probability=True, random_state=42) # Puedes probar con kernel='linear'

# Entrenamos el modelo usando el conjunto de entrenamiento.
model.fit(X_train, y_train)

print("--- Modelo Entrenado Exitosamente ---\n")

# ==============================================================================
# 3. Realizar Predicciones y Evaluar el Rendimiento del Modelo
# ==============================================================================
# Predecimos las clases (0 o 1) para el conjunto de prueba.
y_pred = model.predict(X_test)
# Predecimos las probabilidades para la clase positiva (clase 1, 'virginica') para la curva ROC.
y_prob = model.predict_proba(X_test)[:, 1]

# Calculamos métricas de evaluación comunes para clasificación.
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_prob) # Área bajo la curva ROC

print("--- Métricas de Evaluación del Modelo en el Conjunto de Prueba ---")
print(f"Exactitud (Accuracy): {accuracy:.4f}")
print(f"Precisión (Precision): {precision:.4f}")
print(f"Sensibilidad/Recall (Recall): {recall:.4f}")
print(f"Puntuación F1 (F1-Score): {f1:.4f}")
print(f"Área bajo la Curva ROC (AUC-ROC): {roc_auc:.4f}\n")

print("--- Interpretación de las Métricas ---")
print(f"  Exactitud: Proporción de predicciones correctas en total. {accuracy*100:.2f}% de muestras bien clasificadas.")
print(f"  Precisión: Relevancia de las predicciones positivas. De las que dijo '{selected_target_names[1]}', el {precision*100:.2f}% fueron correctas.")
print(f"  Recall: Capacidad de encontrar todas las instancias positivas. De todas las '{selected_target_names[1]}' reales, encontró el {recall*100:.2f}%.")
print("  F1-Score: Balance entre Precisión y Recall, útil en clases desbalanceadas.")
print(f"  AUC-ROC: Capacidad discriminativa del modelo. Un valor de {roc_auc:.2f} (cercano a 1) indica una excelente capacidad para distinguir entre '{selected_target_names[0]}' y '{selected_target_names[1]}'.\n")


# ==============================================================================
# 4. Visualización de la Matriz de Confusión
# ==============================================================================
# La matriz de confusión muestra el recuento de aciertos y errores por clase.
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=selected_target_names)
disp.plot(cmap=plt.cm.cividis, ax=plt.gca(), values_format='d') # Puedes cambiar 'cividis', 'Blues', 'viridis', etc.
plt.title('Matriz de Confusión', fontsize=14, fontweight='bold')
plt.xlabel('Clase Predicha', fontsize=12)
plt.ylabel('Clase Real', fontsize=12)
plt.show()

print("\n--- Interpretación de la Matriz de Confusión ---")
print(f"  Verdaderos Negativos (TN): {cm[0, 0]} (Predijo '{selected_target_names[0]}' y era '{selected_target_names[0]}')")
print(f"  Falsos Positivos (FP): {cm[0, 1]} (Predijo '{selected_target_names[1]}' pero era '{selected_target_names[0]}')")
print(f"  Falsos Negativos (FN): {cm[1, 0]} (Predijo '{selected_target_names[0]}' pero era '{selected_target_names[1]}')")
print(f"  Verdaderos Positivos (TP): {cm[1, 1]} (Predijo '{selected_target_names[1]}' y era '{selected_target_names[1]}')\n")
print("Un modelo perfecto tendría valores solo en la diagonal (TN y TP), y cero en FP y FN.")


# ==============================================================================
# 5. Gráficas de Apoyo: Frontera de Decisión y Curva ROC
# ==============================================================================
print("--- Generando Gráficas de Apoyo ---\n")

# Gráfica 1: Frontera de Decisión (solo posible en 2D)
# Definimos el rango para el gráfico
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

# Realizamos predicciones sobre la malla para dibujar la frontera
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(9, 6))
plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.coolwarm) # Área sombreada para las clases
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, edgecolor='k', s=20) # Puntos de datos
plt.title(f'Frontera de Decisión de SVM (Kernel={model.kernel})', fontsize=14, fontweight='bold')
plt.xlabel(selected_feature_names[0], fontsize=12)
plt.ylabel(selected_feature_names[1], fontsize=12)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.xticks([])
plt.yticks([])
plt.show()

print("\nInterpretación de la Gráfica 1 (Frontera de Decisión):")
print("Esta gráfica muestra cómo el SVM ha dividido el espacio de características. La línea (o curva)")
print("de separación es la 'frontera de decisión'. Los puntos de datos que caen en las áreas sombreadas")
print("corresponden a la clasificación que el modelo asignaría. El 'margen' del SVM es la banda alrededor")
print(" de esta frontera donde se encuentran los vectores de soporte (los puntos clave que definen la frontera).")
print("Al usar un kernel RBF (no lineal), esta frontera puede ser curva.\n")


# Gráfica 2: Curva ROC (Receiver Operating Characteristic)
# Muestra la capacidad del modelo para distinguir entre las dos clases.
fpr, tpr, thresholds = roc_curve(y_test, y_prob) # false positive rate, true positive rate

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'Curva ROC (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Clasificador Aleatorio') # Línea de referencia
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('Tasa de Falsos Positivos (FPR)', fontsize=12)
plt.ylabel('Tasa de Verdaderos Positivos (TPR) / Sensibilidad', fontsize=12)
plt.title('Curva ROC para SVM', fontsize=14, fontweight='bold')
plt.legend(loc="lower right")
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()

print("\nInterpretación de la Gráfica 2 (Curva ROC):")
print("La Curva ROC representa la relación entre la Tasa de Verdaderos Positivos (TPR) y la Tasa de Falsos Positivos (FPR) en diferentes umbrales.")
print("Un modelo perfecto tendría una curva que sube directamente a la esquina superior izquierda (AUC=1.0).")
print("La línea diagonal punteada (AUC=0.5) representa un clasificador que adivina aleatoriamente.")
print(f"Nuestro modelo, con un AUC de {roc_auc:.2f}, está muy por encima de la línea aleatoria, indicando una excelente capacidad de discriminación.\n")

