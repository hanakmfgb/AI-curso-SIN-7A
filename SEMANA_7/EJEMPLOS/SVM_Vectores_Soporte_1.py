import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, roc_curve,
    confusion_matrix, ConfusionMatrixDisplay
)


# Si ya tienes el archivo 'diabetes.csv', puedes saltar este bloque.
# Aquí lo creamos en memoria para simular la carga.
df = pd.read_csv('diabetes.csv')
# Para leer un archivo real usa: df = pd.read_csv('diabetes.csv')

# ==============================================================================
# 1. Carga del Dataset y Preparación de Datos
# ==============================================================================
print("--- Información del Dataset de Diabetes ---")
print(f"Número total de muestras: {df.shape[0]}")
print(f"Número total de características: {df.shape[1] - 1}") # -1 por la columna Target
print(f"Primeras 5 filas:\n{df.head()}\n")

# Separamos características (X) y variable objetivo (y)
feature_cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
                'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
X = df[feature_cols].values
y = df['Outcome'].values

# Definimos los nombres para las gráficas
target_names = ['No Diabetes', 'Diabetes']

# IMPORTANTE: Escalado de Datos
# SVM es muy sensible a la escala de los datos (Ej: Insulina llega a 800, Edad a 60).
# Si no escalamos, la variable con números más grandes dominará el modelo.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividimos el conjunto de datos en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)

print("--- Dimensiones de los conjuntos de datos (Escalados) ---")
print(f"X_train: {X_train.shape}, y_train: {y_train.shape}")
print(f"X_test:  {X_test.shape},  y_test:  {y_test.shape}\n")

# ==============================================================================
# 2. Construcción y Entrenamiento del Modelo de SVM (SVC)
# ==============================================================================
# Usamos un kernel RBF. SVM busca el hiperplano óptimo en un espacio multidimensional.
model = SVC(kernel='rbf', gamma='scale', C=1.0, probability=True, random_state=42)

# Entrenamos el modelo con TODAS las características
model.fit(X_train, y_train)

print("--- Modelo SVM Entrenado Exitosamente (con 8 características) ---\n")

# ==============================================================================
# 3. Realizar Predicciones y Evaluar el Rendimiento
# ==============================================================================
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1] # Probabilidad de clase positiva (Diabetes)

# Métricas
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_prob)

print("--- Métricas de Evaluación ---")
print(f"Exactitud (Accuracy): {accuracy:.4f}")
print(f"Precisión:            {precision:.4f}")
print(f"Sensibilidad (Recall):{recall:.4f}")
print(f"F1-Score:             {f1:.4f}")
print(f"AUC-ROC:              {roc_auc:.4f}\n")

# ==============================================================================
# 4. Visualización de la Matriz de Confusión
# ==============================================================================
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=target_names)
disp.plot(cmap=plt.cm.Blues, ax=plt.gca(), values_format='d')
plt.title('Matriz de Confusión: Diabetes', fontsize=14, fontweight='bold')
plt.show()

# ==============================================================================
# 5. Gráficas de Apoyo: Curva ROC y Frontera de Decisión (Especial)
# ==============================================================================
print("--- Generando Gráficas de Apoyo ---\n")

# --- Gráfica A: Curva ROC ---
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'Curva ROC (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('Tasa de Falsos Positivos (FPR)')
plt.ylabel('Tasa de Verdaderos Positivos (TPR)')
plt.title('Curva ROC - Capacidad de Diagnóstico')
plt.legend(loc="lower right")
plt.grid(True, alpha=0.3)
plt.show()

# --- Gráfica B: Frontera de Decisión (Visualización 2D) ---
# NOTA EXPERTA: El modelo original usa 8 dimensiones. No podemos dibujar 8 ejes en una pantalla 2D.
# Para mostrar la "frontera", entrenaremos un SEGUNDO modelo temporal usando solo
# las 2 características más visuales: Glucosa (índice 1) y BMI (índice 5).

print("Generando visualización 2D (Simplificación usando solo Glucosa y BMI)...")

# Índices de Glucose y BMI
idx_viz = [1, 5] 
X_viz = X[:, idx_viz] # Tomamos los datos crudos de esas dos columnas
y_viz = y

# Re-escalamos solo estas 2 columnas para la visualización
scaler_viz = StandardScaler()
X_viz_scaled = scaler_viz.fit_transform(X_viz)

# Entrenamos un modelo 2D solo para el gráfico
model_viz = SVC(kernel='rbf', C=1.0, gamma='auto')
model_viz.fit(X_viz_scaled, y_viz)

# Crear malla para el gráfico
x_min, x_max = X_viz_scaled[:, 0].min() - 0.5, X_viz_scaled[:, 0].max() + 0.5
y_min, y_max = X_viz_scaled[:, 1].min() - 0.5, X_viz_scaled[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

Z = model_viz.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(9, 6))
plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.coolwarm)
# Graficamos los puntos reales
scatter = plt.scatter(X_viz_scaled[:, 0], X_viz_scaled[:, 1], c=y_viz, 
                      cmap=plt.cm.coolwarm, edgecolor='k', s=40)
plt.title('Frontera de Decisión SVM (Simplificado: Glucosa vs BMI)', fontsize=14, fontweight='bold')
plt.xlabel('Glucosa (Estandarizada)')
plt.ylabel('BMI (Estandarizado)')
plt.legend(handles=scatter.legend_elements()[0], labels=target_names)
plt.show()

print("\nInterpretación:")
print("La gráfica de frontera muestra cómo el modelo separaría a los pacientes si solo tuviera")
print("en cuenta la Glucosa y el BMI. Las zonas rojas indican alta probabilidad de diabetes")
print("y las azules baja probabilidad. Observa cómo el modelo trata de envolver los casos positivos.")