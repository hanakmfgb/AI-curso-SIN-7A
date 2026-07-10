# Ejemplo de matriz 2D
matriz_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Dimensiones de la matriz (filas x columnas)
num_filas = len(matriz_2d)
num_columnas = len(matriz_2d[0])  # Asumimos que todas las filas tienen la misma longitud

print(f"Matriz 2D: {matriz_2d}")
print(f"Dimensiones: {num_filas}x{num_columnas}")

# Acceder al elemento en la fila 1, columna 2 
elemento = matriz_2d[0][1]
print(f"Elemento en [0][1]: {elemento}")  # Imprimirá 2

