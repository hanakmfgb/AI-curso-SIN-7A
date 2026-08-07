# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 23:05:12 2025

@author: MARCELOFGB
"""
class Nodo:
    def __init__(self, ciudad):
        self.ciudad = ciudad
        self.vecinos = {}  # Diccionario: {ciudad_vecina: precio}

class Grafo:
    def __init__(self):
        self.nodos = {}  # Diccionario: {nombre_ciudad: objeto_Nodo}

    def agregar_nodo(self, ciudad):
        if ciudad not in self.nodos:
            self.nodos[ciudad] = Nodo(ciudad)

    def agregar_arista(self, ciudad1, ciudad2, precio):
        if ciudad1 in self.nodos and ciudad2 in self.nodos:
            self.nodos[ciudad1].vecinos[ciudad2] = precio
            self.nodos[ciudad2].vecinos[ciudad1] = precio  # Asumimos vuelos bidireccionales

    def obtener_precio(self, ciudad1, ciudad2):
        if ciudad1 in self.nodos and ciudad2 in self.nodos:
            if ciudad2 in self.nodos[ciudad1].vecinos:
                return self.nodos[ciudad1].vecinos[ciudad2]
        return float('inf')  # Precio infinito si no hay vuelo directo

    def buscar_ruta(self, inicio, destino, presupuesto):
        """Busca rutas directas y con una escala, dentro del presupuesto."""
        rutas = []

        # Vuelos directos
        precio_directo = self.obtener_precio(inicio, destino)
        if precio_directo <= presupuesto:
            rutas.append(([inicio, destino], precio_directo))

        # Vuelos con una escala
        for ciudad_intermedia in self.nodos:
            if ciudad_intermedia != inicio and ciudad_intermedia != destino:
                precio_tramo1 = self.obtener_precio(inicio, ciudad_intermedia)
                precio_tramo2 = self.obtener_precio(ciudad_intermedia, destino)
                precio_total = precio_tramo1 + precio_tramo2
                if precio_total <= presupuesto and precio_total != float('inf'):
                    rutas.append(([inicio, ciudad_intermedia, destino], precio_total))

        return rutas

# Crear el grafo (base de conocimiento)
grafo_vuelos = Grafo()
grafo_vuelos.agregar_nodo("Madrid")
grafo_vuelos.agregar_nodo("París")
grafo_vuelos.agregar_nodo("Roma")
grafo_vuelos.agregar_nodo("Londres")
grafo_vuelos.agregar_nodo("Berlín")

grafo_vuelos.agregar_arista("Madrid", "París", 150)
grafo_vuelos.agregar_arista("Madrid", "Roma", 180)
grafo_vuelos.agregar_arista("Madrid", "Londres", 120)
grafo_vuelos.agregar_arista("París", "Berlín", 100)
grafo_vuelos.agregar_arista("Roma", "Berlín", 200)
grafo_vuelos.agregar_arista("Londres", "Berlín", 140)

# Interfaz de usuario
print("Destinos disponibles:")
print("---------------------")
print("Ciudad   | Precio desde Madrid")
print("---------------------")
for ciudad in grafo_vuelos.nodos:
    if ciudad != "Madrid":
        precio = grafo_vuelos.obtener_precio("Madrid", ciudad)
        if precio != float('inf'):
            print(f"{ciudad:8} | {precio}")
        else:
            print(f"{ciudad:8} | No disponible")

destino = input("\nIngrese el destino deseado: ")
presupuesto = float(input("Ingrese su presupuesto máximo: "))

# Inferencia y resultados
rutas_encontradas = grafo_vuelos.buscar_ruta("Madrid", destino, presupuesto)

if rutas_encontradas:
    print("\nRutas encontradas dentro de su presupuesto:")
    for ruta, precio in rutas_encontradas:
        print(f"Ruta: {ruta} - Precio: {precio}")
else:
    print("No se encontraron rutas dentro de su presupuesto.")