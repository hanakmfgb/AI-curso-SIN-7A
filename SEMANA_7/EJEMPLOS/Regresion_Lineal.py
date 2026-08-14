import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

#from sklearn.datasets import load_diabetes # Importamos el dataset de diabetes

# ==============================================================================
# 1. Carga del Dataset y Preparación de Datos
# ==============================================================================
# Cargamos el conjunto de datos de diabetes.
# Este dataset contiene 10 características fisiológicas y la progresión de la enfermedad.
diabetes = pd.read_csv('student_scores.csv')
#diabetes = load_diabetes()
#X = diabetes.data  # Características (variables independientes)
#y = diabetes.target # Variable objetivo (progresión de la enfermedad, valor continuo)
X = diabetes.drop('Scores', axis=1)
y = diabetes['Scores']
feature_names = diabetes.columns #.feature_names # Nombres de las características para mejor interpretabilidad

print("--- Información del Dataset de Estudiantes ---")
print(f"Número de observaciones (pacientes): {X.shape[0]}")
print(f"Número de características (variables independientes): {X.shape[1]}")
print(f"Nombres de las características: {feature_names}\n")

# Dividimos el conjunto de datos en entrenamiento y prueba.
# - X_train, y_train: Utilizados para entrenar el modelo.
# - X_test, y_test: Utilizados para evaluar el modelo con datos no vistos.
# test_size=0.2 indica que el 20% de los datos se usarán para prueba.
# random_state=42 asegura que la división sea la misma cada vez que se ejecuta el código (reproducibilidad).
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("--- Dimensiones de los conjuntos de datos ---")
print(f"Dimensiones de X_train (características para entrenamiento): {X_train.shape}")
print(f"Dimensiones de y_train (objetivo para entrenamiento): {y_train.shape}")
print(f"Dimensiones de X_test (características para prueba): {X_test.shape}")
print(f"Dimensiones de y_test (objetivo para prueba): {y_test.shape}\n")

# ==============================================================================
# 2. Construcción y Entrenamiento del Modelo de Regresión Lineal Múltiple
# ==============================================================================
# Creamos una instancia del modelo de Regresión Lineal.
# Scikit-learn automáticamente maneja la regresión múltiple si X tiene más de una columna.
model = LinearRegression()

# Entrenamos el modelo usando el conjunto de entrenamiento.
# El método 'fit' calcula los valores óptimos para los coeficientes (βs) y el intercepto (β0).
model.fit(X_train, y_train)

print("--- Modelo Entrenado Exitosamente ---\n")

# ==============================================================================
# 3. Interpretación de los Coeficientes del Modelo Aprendido
# ==============================================================================
# Los coeficientes (model.coef_) representan los pesos (βj) que el modelo asigna a cada característica.
# El intercepto (model.intercept_) es el valor de β0.
print("--- Coeficientes e Intercepto del Modelo Inferred ---")
for i, coef in enumerate(model.coef_):
    print(f"  Coeficiente para '{feature_names[i]}': {coef:.2f}")
print(f"  Intercepto (β0): {model.intercept_:.2f}\n")

# Reconstruimos la ecuación lineal aprendida para mayor claridad en la interpretación.
# y_pred = β0 + β1*x1 + β2*x2 + ... + βp*xp
equation_terms = [f"{model.intercept_:.2f}"]
for i, coef in enumerate(model.coef_):
    sign = "+" if coef >= 0 else "-"
    equation_terms.append(f"{sign} {abs(coef):.2f} * {feature_names[i]}")
print("--- Ecuación del Modelo Lineal Inferred ---")
print(f"y_pred = {' '.join(equation_terms)}\n")

print("Interpretación de los Coeficientes:")
print("Cada coeficiente indica cómo cambia la progresión de la enfermedad por cada unidad de aumento en la característica correspondiente, manteniendo las demás constantes.")
print("Un coeficiente positivo indica una relación directa (aumenta la característica, aumenta y_pred).")
print("Un coeficiente negativo indica una relación inversa (aumenta la característica, disminuye y_pred).\n")

# ==============================================================================
# 4. Realizar Predicciones y Evaluar el Rendimiento del Modelo
# ==============================================================================
# Usamos el modelo entrenado para predecir los valores de 'y' para el conjunto de prueba (datos no vistos).
y_pred = model.predict(X_test)

# Calculamos algunas métricas de evaluación comunes para problemas de regresión.
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse) # RMSE es la raíz cuadrada del MSE, más fácil de interpretar.
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("--- Métricas de Evaluación del Modelo en el Conjunto de Prueba ---")
print(f"Error Cuadrático Medio (MSE): {mse:.2f}")
print(f"Raíz del Error Cuadrático Medio (RMSE): {rmse:.2f}")
print(f"Error Absoluto Medio (MAE): {mae:.2f}")
print(f"Coeficiente de Determinación (R^2): {r2:.2f}\n")

print("--- Interpretación de las Métricas ---")
print("MSE y RMSE: Cuantifican el promedio de los errores al cuadrado (MSE) y en la unidad original (RMSE). Cuanto más bajos, mejor.")
print("MAE: Mide el error promedio absoluto. Es menos sensible a valores atípicos que MSE/RMSE.")
print("R^2: Indica la proporción de la varianza en la variable objetivo que es 'explicada' por las características. Un valor de 1 es perfecto, 0 significa que el modelo no es mejor que predecir la media de 'y'. Un R^2 de {r2:.2f} sugiere que el {r2*100:.1f}% de la varianza en la progresión de la diabetes es explicada por nuestras características.\n")

# ==============================================================================
# 5. Gráficas de Apoyo para Visualizar el Rendimiento
# ==============================================================================
print("--- Generando Gráficas de Apoyo ---")

# Gráfica 1: Valores Reales vs. Valores Predichos
# Un buen modelo de regresión tendrá los puntos agrupados cerca de la línea diagonal (y=x).
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.7, color='skyblue', label='Predicciones')
# Añadimos una línea diagonal que representa la predicción perfecta
plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', linestyle='--', linewidth=2, label='Predicción Perfecta (y=x)')
plt.title('Valores Reales (y_test) vs. Valores Predichos (y_pred)', fontsize=14, fontweight='bold')
plt.xlabel('Progresión Real de la Enfermedad', fontsize=12)
plt.ylabel('Progresión Predicha por el Modelo', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()

print("\nInterpretación de la Gráfica 1 (Valores Reales vs. Predichos):")
print("Esta gráfica permite visualizar la nube de puntos de las predicciones frente a los valores reales.")
print("Cuanto más cerca se agrupen los puntos alrededor de la línea diagonal roja, mejor será el ajuste y la precisión del modelo.")
print("Una dispersión amplia alrededor de la línea indica que el modelo tiene dificultades para predecir con exactitud.\n")


# Gráfica 2: Análisis de Residuos (Errores de Predicción)
# Los residuos (errores = real - predicho) deben distribuirse aleatoriamente alrededor de la línea de cero.
residuals = y_test - y_pred
plt.figure(figsize=(10, 6))
plt.scatter(y_pred, residuals, alpha=0.7, color='lightcoral', label='Residuos')
# Añadimos una línea horizontal en y=0, que es el valor esperado del residuo en un modelo ideal.
plt.axhline(y=0, color='darkgreen', linestyle='-', linewidth=2, label='Línea de Residuo Cero')
plt.title('Análisis de Residuos (Valores Predichos vs. Errores)', fontsize=14, fontweight='bold')
plt.xlabel('Valores Predichos por el Modelo', fontsize=12)
plt.ylabel('Residuos (Error = Real - Predicho)', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()

print("Interpretación de la Gráfica 2 (Análisis de Residuos):")
print("Esta gráfica es fundamental para diagnosticar la validez del modelo lineal.")
print("Un modelo bien ajustado muestra los residuos dispersos aleatoriamente alrededor de la línea horizontal de cero, sin patrón aparente.")
print("Si se observa un patrón (por ejemplo, forma de embudo, curva, aglomeraciones), podría indicar que el modelo lineal no es el más adecuado,")
print("que le faltan variables importantes, o que no se cumplen los supuestos de la regresión lineal (como la homocedasticidad).\n")

