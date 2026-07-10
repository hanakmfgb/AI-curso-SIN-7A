# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 17:49:13 2025

@author: MARCELOFGB
"""

traductor = {
    "hello": "hola",
    "goodbye": "adiós",
    "dog": "perro",
    "cat": "gato",
    "house": "casa"
}

def traducir(palabra):
    palabra = palabra.lower()  # Convertir a minúsculas para que la búsqueda sea insensible a mayúsculas/minúsculas
    if palabra in traductor:
        return traductor[palabra]
    else:
        return "Lo siento, no conozco esa palabra."

palabra_a_traducir = input("Escribe una palabra en inglés: ")
traduccion = traducir(palabra_a_traducir)
print(f"La traducción de '{palabra_a_traducir}' es: {traduccion}")


