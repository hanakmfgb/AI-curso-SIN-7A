import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, plot_tree # Importamos Regressor, no Classifier
from sklearn.metrics import mean_squared_error, mean_absolute_error
import time
import tracemalloc # Librería estándar para rastrear memoria RAM

# ==============================================================================
# 1. Carga del Dataset (Simulada desde tu muestra)
# ==============================================================================

# Leemos el CSV
df = pd.read_csv('StudentPerformanceFactors.csv')


print("--- Muestra del Dataset ---")
print(df.head())
print("\n--- Información de Tipos de Datos ---")
print(df.info())

# ==============================================================================
# 2. Preprocesamiento de Datos (CRÍTICO EN ESTE DATASET)
# ==============================================================================
# Separamos las características (X) y la variable objetivo (y)
X = df.drop('Exam_Score', axis=1)
y = df['Exam_Score']

print(f"\nDimensiones originales de X: {X.shape}")

# PROBLEMA: Scikit-learn no entiende "Low", "High", "Male", etc.
# SOLUCIÓN: One-Hot Encoding. Convierte columnas de texto en columnas numéricas (0 y 1).
# Ejemplo: La columna "Gender" se convierte en "Gender_Male" (1 si es hombre, 0 si no).
X_encoded = pd.get_dummies(X, drop_first=True)

print(f"Dimensiones de X después del Encoding: {X_encoded.shape}")
print("Nota: El número de columnas aumentó porque las variables categóricas se desglosaron.\n")

# Dividimos en entrenamiento y prueba
# Al ser un dataset tan pequeño (7 filas), dejamos pocas para test para que el modelo pueda aprender algo.
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# ==============================================================================
# 3. Entrenamiento del Árbol de Regresión
# ==============================================================================
# Instanciamos el modelo.
# max_depth=5: Limitamos la profundidad para evitar que el árbol memorice los datos (overfitting),
# aunque con 7 datos el árbol será pequeño de todos modos.
regressor = DecisionTreeRegressor(random_state=42, max_depth=5)

# Entrenamos
regressor.fit(X_train, y_train)

print("--- Modelo de Árbol de Regresión Entrenado ---")

# ==============================================================================
# 4. Predicción y Evaluación
# ==============================================================================
# Predecimos las notas
y_pred = regressor.predict(X_test)

print("\n--- Comparación Real vs Predicción ---")
comparativa = pd.DataFrame({'Nota Real': y_test, 'Nota Predicha': y_pred})
print(comparativa)

# Métricas de Regresión
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)

print("\n--- Métricas de Error ---")
print(f"MAE (Error Absoluto Medio): {mae:.2f}")
print("Interpetación: En promedio, el modelo se equivoca en esta cantidad de puntos.")
print(f"MSE (Error Cuadrático Medio): {mse:.2f}")
print(f"RMSE (Raíz del Error Cuadrático Medio): {rmse:.2f}")


# ==============================================================================
# 5. Visualización del Árbol de Decisión
# ==============================================================================
print("\n--- Generando Gráfico del Árbol ---")
plt.figure(figsize=(15, 8))
plot_tree(regressor, 
          feature_names=X_encoded.columns, 
          filled=True, 
          rounded=True, 
          precision=2)
plt.title("Árbol de Decisión para Predecir Notas (Exam_Score)")
plt.show()

print("\nInterpretación del Árbol:")
print("- Cada recuadro es un 'nodo'.")
print("- La primera línea de cada nodo es la pregunta (ej: Previous_Scores <= 80).")
print("- 'mse': El error cuadrático en ese nodo (cuanto más bajo, más puro es el grupo).")
print("- 'value': Es la predicción de nota promedio para los estudiantes que caen en ese nodo.")
print("- El color más oscuro indica valores de nota más altos.")

# ==============================================================================
# 6. Gráfico de Importancia de las Características
# ==============================================================================
# Nos dice qué variables fueron más útiles para decidir la nota
importances = regressor.feature_importances_
indices = np.argsort(importances)[::-1] # Ordenar de mayor a menor

plt.figure(figsize=(10, 6))
plt.title("Importancia de las Variables en la Predicción de la Nota")
plt.bar(range(X_train.shape[1]), importances[indices], align="center")
plt.xticks(range(X_train.shape[1]), X_encoded.columns[indices], rotation=90)
plt.tight_layout()
plt.show()


# ==============================================================================
# 7. Evaluación de Performance Computacional y Métricas Adicionales
# ==============================================================================

print("\n" + "="*80)
print(" REPORTE DE RENDIMIENTO COMPUTACIONAL Y METRICAS FINALES")
print("="*80)

# 1. Métrica de Performance del Modelo: R2 Score
# El R2 indica qué tan bien se ajusta el modelo a los datos (1.0 es perfecto, 0.0 es aleatorio)
from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_pred)
print("--- Calidad del Modelo ---")
print(f"Coeficiente de Determinación (R²): {r2:.4f}")
print("Interpretación: Un R² cercano a 1 indica que el modelo explica bien la varianza de las notas.\n")

# 2. Medición de Recursos (Tiempo y Memoria)
# Para medirlo con precisión, re-ejecutamos el proceso de entrenamiento y predicción dentro de un monitor.

print("--- Consumo de Recursos (Benchmark) ---")

# Iniciar el rastreo de asignación de memoria
tracemalloc.start()

# Capturar tiempo de inicio
start_time = time.perf_counter() 

# --- PROCESO A MEDIR (Entrenamiento + Predicción) ---
model_benchmark = DecisionTreeRegressor(random_state=42, max_depth=5)
model_benchmark.fit(X_train, y_train)
_ = model_benchmark.predict(X_test)
# ----------------------------------------------------

# Capturar tiempo de finalización
end_time = time.perf_counter()

# Capturar uso de memoria (actual, pico máximo)
current, peak = tracemalloc.get_traced_memory()

# Detener el rastreo
tracemalloc.stop()

# Cálculos finales
execution_time = end_time - start_time
peak_memory_mb = peak / 1024 / 1024 # Convertir bytes a Megabytes

print(f"Tiempo de Ejecución: {execution_time:.6f} segundos")
print(f"Memoria RAM Pico utilizada: {peak_memory_mb:.6f} MB")
print("-" * 80)