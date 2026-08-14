import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer # Dataset de cáncer de mama
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, # Métricas de clasificación
    roc_auc_score, roc_curve, # Para la Curva ROC
    confusion_matrix, ConfusionMatrixDisplay # Para la Matriz de Confusión
)

# ==============================================================================
# 1. Carga del Dataset y Preparación de Datos
# ==============================================================================
# Cargamos el conjunto de datos de cáncer de mama.
# Este dataset es binario (0: benigno, 1: maligno) y contiene 30 características.
cancer = load_breast_cancer()
X = cancer.data          # Características (variables independientes)
y = cancer.target        # Variable objetivo (0 o 1 para clase 'benigna' o 'maligna')
feature_names = cancer.feature_names # Nombres de las características
target_names = cancer.target_names   # Nombres de las clases (Benigno, Maligno)

print("--- Información del Dataset de Cáncer de Mama ---")
print(f"Número de observaciones (muestras): {X.shape[0]}")
print(f"Número de características: {X.shape[1]}")
print(f"Nombres de las características: \n{feature_names}")
print(f"Nombres de las clases ('{target_names[0]}', '{target_names[1]}'): {target_names}\n")

# Dividimos el conjunto de datos en entrenamiento y prueba.
# - X_train, y_train: Usados para entrenar el modelo.
# - X_test, y_test: Usados para evaluar el modelo con datos no vistos.
# test_size=0.2: 20% de los datos para prueba.
# random_state=42: Para reproducibilidad.
# stratify=y: Muy importante en clasificación para asegurar que las proporciones de clases
#             sean las mismas en los conjuntos de entrenamiento y prueba.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print("--- Dimensiones de los conjuntos de datos ---")
print(f"Dimensiones de X_train (entrenamiento): {X_train.shape}")
print(f"Dimensiones de y_train (entrenamiento): {y_train.shape}")
print(f"Dimensiones de X_test (prueba): {X_test.shape}")
print(f"Dimensiones de y_test (prueba): {y_test.shape}\n")

# ==============================================================================
# 2. Construcción y Entrenamiento del Modelo de Regresión Logística
# ==============================================================================
# Creamos una instancia del modelo de Regresión Logística.
# max_iter=1000: Aumentamos las iteraciones para asegurar la convergencia del algoritmo.
# random_state=42: Para reproducibilidad.
model = LogisticRegression(max_iter=100, random_state=42)

# Entrenamos el modelo usando el conjunto de entrenamiento.
# El método 'fit' aprende los coeficientes (pesos) y el intercepto.
model.fit(X_train, y_train)

print("--- Modelo Entrenado Exitosamente ---\n")

# ==============================================================================
# 3. Realizar Predicciones y Evaluar el Rendimiento del Modelo
# ==============================================================================
# Predecimos las clases (0 o 1) para el conjunto de prueba.
y_pred = model.predict(X_test)
# Predecimos las probabilidades para la clase positiva (clase 1) para la curva ROC.
y_prob = model.predict_proba(X_test)[:, 1]

# Calculamos métricas de evaluación comunes para problemas de clasificación.
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_prob)

print("--- Métricas de Evaluación del Modelo en el Conjunto de Prueba ---")
print(f"Exactitud (Accuracy): {accuracy:.4f} (Proporción de predicciones correctas totales)")
print(f"Precisión (Precision): {precision:.4f} (De las que predijimos como Positivas, cuántas fueron realmente Positivas)")
print(f"Sensibilidad/Recall (Recall): {recall:.4f} (De todas las Positivas reales, cuántas predijimos correctamente)")
print(f"Puntuación F1 (F1-Score): {f1:.4f} (Media armónica de Precision y Recall, útil con desbalance de clases)")
print(f"Área bajo la Curva ROC (AUC-ROC): {roc_auc:.4f} (Capacidad del modelo para distinguir entre clases)\n")

print("--- Interpretación General de las Métricas ---")
print(f"Una Exactitud de {accuracy:.4f} significa que el modelo clasificó correctamente el {accuracy*100:.2f}% de las muestras.")
print("La Precisión, Recall y F1-Score son importantes para entender el rendimiento en cada clase, especialmente la positiva (maligna).")
print(f"Un AUC-ROC de {roc_auc:.4f} (cercano a 1) indica que el modelo tiene una excelente capacidad para diferenciar entre pacientes con cáncer maligno y benigno.")

# ==============================================================================
# 4. Visualización de la Matriz de Confusión
# ==============================================================================
# La matriz de confusión muestra el número de verdaderos positivos, verdaderos negativos,
# falsos positivos y falsos negativos.
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))
# Usamos ConfusionMatrixDisplay para una visualización más fácil y legible.
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=target_names)
disp.plot(cmap=plt.cm.Blues, ax=plt.gca(), values_format='d') # d para mostrar enteros
plt.title('Matriz de Confusión', fontsize=14, fontweight='bold')
plt.xlabel('Clase Predicha', fontsize=12)
plt.ylabel('Clase Real', fontsize=12)
plt.show()

print("\n--- Interpretación de la Matriz de Confusión ---")
print(f"  Verdaderos Negativos (TN): {cm[0, 0]} (Predijo {target_names[0]} y era {target_names[0]})")
print(f"  Falsos Positivos (FP): {cm[0, 1]} (Predijo {target_names[1]} pero era {target_names[0]})")
print(f"  Falsos Negativos (FN): {cm[1, 0]} (Predijo {target_names[0]} pero era {target_names[1]})")
print(f"  Verdaderos Positivos (TP): {cm[1, 1]} (Predijo {target_names[1]} y era {target_names[1]})\n")
print("Idealmente, queremos muchos TN y TP, y pocos FP y FN.")

# ==============================================================================
# 5. Gráfica de Apoyo: Curva ROC
# ==============================================================================
# La Curva ROC (Receiver Operating Characteristic) ilustra el rendimiento de clasificación
# en todos los posibles umbrales de discriminación.
# 'fpr' = Tasa de Falsos Positivos, 'tpr' = Tasa de Verdaderos Positivos.
fpr, tpr, thresholds = roc_curve(y_test, y_prob)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'Curva ROC (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--') # Línea de clasificador aleatorio
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('Tasa de Falsos Positivos (FPR)', fontsize=12) # 1 - Especificidad
plt.ylabel('Tasa de Verdaderos Positivos (TPR) / Sensibilidad', fontsize=12) # Recall
plt.title('Curva ROC de Regresión Logística', fontsize=14, fontweight='bold')
plt.legend(loc='lower right')
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()

print("\n--- Interpretación de la Curva ROC ---")
print("La Curva ROC muestra la capacidad del modelo para distinguir entre clases.")
print("Cuanto más se acerque la curva a la esquina superior izquierda, mejor es el modelo.")
print("El Área bajo la Curva (AUC-ROC) cuantifica esto; un valor de 1 es perfecto, 0.5 es un clasificador aleatorio (línea discontinua azul).")
print(f"Nuestro modelo tiene un AUC de {roc_auc:.2f}, lo cual indica una excelente capacidad discriminativa.\n")