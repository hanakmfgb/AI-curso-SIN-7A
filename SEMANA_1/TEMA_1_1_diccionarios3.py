# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 19:00:09 2025

@author: MARCELOFGB
"""

estudiante = {
    "nombre": "Ana",
    "edad": 20,
    "carrera": "Ingeniería"
}
nuevos_datos = {
    "edad": 21,  # Actualizar la edad
    "ciudad": "Madrid"  # Agregar la ciudad
}
estudiante.update(nuevos_datos)
print(estudiante)  
# Output: {'nombre': 'Ana', 'edad': 21, 'carrera': 'Ingeniería', 'ciudad': 'Madrid'}
 
tienda1 = {
    "manzanas": 10,
    "platanos": 5,
    "naranjas": 12
}
tienda2 = {
    "peras": 8,
    "platanos": 15,  # Cantidad diferente en la tienda 2
    "uvas": 20
}
tienda1.update(tienda2)
print(tienda1)
# Output: {'manzanas': 10, 'platanos': 15, 'naranjas': 12, 'peras': 8, 'uvas': 20}
