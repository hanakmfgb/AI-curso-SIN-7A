# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 19:54:35 2025

@author: MARCELOFGB
"""

import networkx as nx
import matplotlib.pyplot as plt

class Proposicion:
    def __init__(self, nombre, valor=None):
        self.nombre = nombre
        self.valor = valor  # True, False, o None (desconocido)

    def __repr__(self):
        return f"{self.nombre}: {self.valor}"

class Regla:
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente  # Lista de proposiciones (AND)
        self.consecuente = consecuente  # Proposición

    def __repr__(self):
        antecedente_str = " AND ".join([p.nombre for p in self.antecedente])
        return f"IF {antecedente_str} THEN {self.consecuente.nombre}"

class BaseConocimiento:
    def __init__(self):
        self.proposiciones = {}  # Diccionario de nombre: Proposicion
        self.reglas = []
        self.grafo = nx.DiGraph()  # Grafo dirigido para representar las relaciones

    def agregar_proposicion(self, nombre):
        if nombre not in self.proposiciones:
            prop = Proposicion(nombre)
            self.proposiciones[nombre] = prop
            self.grafo.add_node(nombre)  # Agrega el nodo al grafo
            return prop
        return self.proposiciones[nombre]

    def agregar_regla(self, antecedente_nombres, consecuente_nombre):
        antecedentes = [self.proposiciones[nombre] for nombre in antecedente_nombres]
        consecuente = self.proposiciones[consecuente_nombre]
        regla = Regla(antecedentes, consecuente)
        self.reglas.append(regla)
        for ant in antecedente_nombres:
            self.grafo.add_edge(ant, consecuente_nombre) # Agrega arista al grafo
        return regla

    def inferir(self):
        cambios = True
        while cambios:
            cambios = False
            for regla in self.reglas:
                if all(prop.valor == True for prop in regla.antecedente):
                    if regla.consecuente.valor != True:
                        regla.consecuente.valor = True
                        cambios = True
                        print(f"Inferencia: {regla.consecuente.nombre} se establece como VERDADERO")

    def obtener_valor_proposicion(self, nombre):
        if nombre in self.proposiciones:
            return self.proposiciones[nombre].valor
        return None

    def establecer_valor_proposicion(self, nombre, valor):
        if nombre in self.proposiciones:
            self.proposiciones[nombre].valor = valor
        else:
            print(f"La proposición '{nombre}' no existe en la base de conocimiento.")

    def visualizar_grafo(self):
        pos = nx.spring_layout(self.grafo)  # Layout para mejor visualización
        nx.draw(self.grafo, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=10, font_weight="bold")
        plt.title("Grafo de Dependencias de la Base de Conocimiento")
        plt.show()

# Inicialización de la base de conocimiento
kb = BaseConocimiento()

# Definición de proposiciones
kb.agregar_proposicion("hojas_amarillas")
kb.agregar_proposicion("manchas_hojas")
kb.agregar_proposicion("tallo_blando")
kb.agregar_proposicion("exceso_riego")
kb.agregar_proposicion("hongos")
kb.agregar_proposicion("planta_enferma")

# Definición de reglas
kb.agregar_regla(["hojas_amarillas", "exceso_riego"], "planta_enferma")
kb.agregar_regla(["manchas_hojas"], "planta_enferma")
kb.agregar_regla(["tallo_blando", "exceso_riego"], "hongos")
kb.agregar_regla(["hongos"], "planta_enferma")

# Interacción con el usuario
print("Bienvenido al sistema de diagnóstico de plantas.")
print("Responda las siguientes preguntas con 'si' o 'no':")

preguntas = {
    "hojas_amarillas": "¿Las hojas están amarillas?",
    "manchas_hojas": "¿Hay manchas en las hojas?",
    "tallo_blando": "¿El tallo está blando?",
    "exceso_riego": "¿Ha regado la planta en exceso?"
}

for prop, pregunta in preguntas.items():
    while True:
        respuesta = input(pregunta + " (si/no): ").lower()
        if respuesta in ["si", "no"]:
            kb.establecer_valor_proposicion(prop, respuesta == "si")
            break
        else:
            print("Respuesta inválida. Por favor, responda con 'si' o 'no'.")

# Inferencia
kb.inferir()

# Resultados
if kb.obtener_valor_proposicion("planta_enferma") == True:
    print("\nDiagnóstico: La planta parece estar enferma.")
    if kb.obtener_valor_proposicion("exceso_riego") == True and kb.obtener_valor_proposicion("hongos") == True:
        print("Causa probable: Exceso de riego y hongos.")
    elif kb.obtener_valor_proposicion("exceso_riego") == True:
        print("Causa probable: Exceso de riego.")
    elif kb.obtener_valor_proposicion("manchas_hojas") == True:
        print("Causa probable: Posible enfermedad por manchas.")
    else:
        print("Causa no determinada con la información proporcionada.")
else:
    print("\nDiagnóstico: La planta parece estar sana.")

# Visualización del grafo
kb.visualizar_grafo()