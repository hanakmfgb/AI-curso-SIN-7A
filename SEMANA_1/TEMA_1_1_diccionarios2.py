# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 18:48:03 2025

@author: MARCELOFGB
"""

# Frase de ejemplo
frase = "esta es una frase de ejemplo para contar palabras esta es una frase"

# Convertir la frase a minúsculas y dividirla en palabras
palabras = frase.lower().split()

# Crear un diccionario para contar las palabras
conteo_palabras = {}

# Iterar sobre las palabras y contar su frecuencia
for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

# Imprimir el diccionario de conteo
print("Conteo de palabras:", conteo_palabras)

# Imprimir el diccionario de una forma más legible
print("\nConteo de palabras (formato legible):")
for palabra, cantidad in conteo_palabras.items():
    print(f"La palabra '{palabra}' aparece {cantidad} veces.")