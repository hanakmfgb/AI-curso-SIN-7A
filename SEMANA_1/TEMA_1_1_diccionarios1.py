# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 18:38:08 2025

@author: MARCELOFGB
"""

# Crear un diccionario para almacenar información de un estudiante
estudiante = {
    "nombre": "Ana",
    "edad": 20,
    "carrera": "Ingeniería",
    "materias": ["Cálculo", "Física", "Programación"]
}

# Acceder a los valores usando las claves
print("Nombre:", estudiante["nombre"])
print("Edad:", estudiante["edad"])
print("Carrera:", estudiante["carrera"])
print("Materias:", estudiante["materias"])

# Imprimir el diccionario completo
print("\nDiccionario completo:", estudiante)

# Imprimir solo las claves
print("\nClaves del diccionario:", estudiante.keys())

# Imprimir solo los valores
print("\nValores del diccionario:", estudiante.values())