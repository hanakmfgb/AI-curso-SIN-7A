# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 21:44:22 2025

@author: MARCELOFGB
"""

#import random
# Funciones auxiliares

def imprimir_tablero(tablero):
    """Imprime el tablero en la consola."""
    print("-------------")
    for i in range(3):
        print("|", tablero[i * 3], "|", tablero[i * 3 + 1], "|", tablero[i * 3 + 2], "|")
        print("-------------")

def verificar_ganador(tablero, jugador):
    """Verifica si el jugador ha ganado."""
    # Filas
    for i in range(3):
        if tablero[i * 3] == tablero[i * 3 + 1] == tablero[i * 3 + 2] == jugador:
            return True
    # Columnas
    for i in range(3):
        if tablero[i] == tablero[i + 3] == tablero[i + 6] == jugador:
            return True
    # Diagonales
    if tablero[0] == tablero[4] == tablero[8] == jugador:
        return True
    if tablero[2] == tablero[4] == tablero[6] == jugador:
        return True
    return False

def tablero_lleno(tablero):
    """Verifica si el tablero está lleno."""
    return all(casilla != " " for casilla in tablero)

def obtener_movimientos_validos(tablero):
    """Devuelve una lista de los índices de las casillas vacías."""
    return [i for i, casilla in enumerate(tablero) if casilla == " "]


# Agentes

def agente_humano(tablero):
    """Pide al usuario que ingrese una posición."""
    while True:
        try:
            posicion = int(input("Ingresa tu movimiento (0-8): "))
            if posicion in obtener_movimientos_validos(tablero):
                return posicion
            else:
                print("Movimiento inválido. Intenta de nuevo.")
        except ValueError:
            print("Ingresa un número válido (0-8).")

def agente_minimax(tablero, jugador):
    """
    Implementa el algoritmo Minimax con poda Alfa-Beta para determinar el mejor movimiento.

    Args:
        tablero: El estado actual del tablero.
        jugador: El jugador para el cual estamos calculando el movimiento (usualmente la IA).

    Returns:
        El índice del mejor movimiento posible.
    """

    def minimax(tablero, jugador, alpha, beta, profundidad=0):
        """Función recursiva Minimax con poda Alfa-Beta."""
        oponente = "O" if jugador == "X" else "X"

        # Casos base: ganador o tablero lleno
        if verificar_ganador(tablero, jugador):
            return 1 # Favorable para el jugador (IA)
        if verificar_ganador(tablero, oponente):
            return -1 # Desfavorable para el jugador (IA)
        if tablero_lleno(tablero):
            return 0 # Empate

        movimientos_validos = obtener_movimientos_validos(tablero)

        if jugador == "X":  # Maximizando (IA)
            mejor_puntaje = -float('inf')
            for movimiento in movimientos_validos:
                tablero[movimiento] = jugador
                puntaje = minimax(tablero, oponente, alpha, beta, profundidad + 1)
                tablero[movimiento] = " "  # Deshacer el movimiento (backtracking)
                mejor_puntaje = max(mejor_puntaje, puntaje)
                alpha = max(alpha, mejor_puntaje)
                if beta <= alpha:
                    break # Poda Beta
            return mejor_puntaje
        else:  # Minimizando (Oponente)
            peor_puntaje = float('inf')
            for movimiento in movimientos_validos:
                tablero[movimiento] = jugador
                puntaje = minimax(tablero, oponente, alpha, beta, profundidad + 1)
                tablero[movimiento] = " "  # Deshacer el movimiento (backtracking)
                peor_puntaje = min(peor_puntaje, puntaje)
                beta = min(beta, peor_puntaje)
                if beta <= alpha:
                    break # Poda Alfa
            return peor_puntaje

    # Encontrar el mejor movimiento para el jugador (IA)
    mejor_movimiento = None
    mejor_puntaje = -float('inf')
    movimientos_validos = obtener_movimientos_validos(tablero)
    alpha = -float('inf')
    beta = float('inf')

    for movimiento in movimientos_validos:
        tablero[movimiento] = jugador
        puntaje = minimax(tablero, "O" if jugador == "X" else "X", alpha, beta) # Evalúa el movimiento actual
        tablero[movimiento] = " "  # Deshacer el movimiento
        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje
            mejor_movimiento = movimiento

    return mejor_movimiento


# Funciones de juego

def jugar_humano_vs_ia(jugador_humano, jugador_ia):
    """Simula un juego entre un humano y la IA."""
    tablero = [" "] * 9
    turno = "X"  # El jugador X comienza

    while True:
        imprimir_tablero(tablero)

        if turno == jugador_humano:
            print("Turno del Humano ({})".format(jugador_humano))
            movimiento = agente_humano(tablero)
        else:
            print("Turno de la IA ({})".format(jugador_ia))
            movimiento = agente_minimax(tablero, turno)

        tablero[movimiento] = turno

        if verificar_ganador(tablero, turno):
            imprimir_tablero(tablero)
            print("¡{} ha ganado!".format(turno))
            break

        if tablero_lleno(tablero):
            imprimir_tablero(tablero)
            print("¡Empate!")
            break

        turno = "O" if turno == "X" else "X"

def jugar_ia_vs_ia(jugador1, jugador2):
    """Simula un juego entre dos agentes IA."""
    tablero = [" "] * 9
    turno = "X"

    while True:
        imprimir_tablero(tablero)
        print("Turno de la IA ({})".format(turno))
        movimiento = agente_minimax(tablero, turno)
        tablero[movimiento] = turno

        if verificar_ganador(tablero, turno):
            imprimir_tablero(tablero)
            print("¡{} ha ganado!".format(turno))
            break

        if tablero_lleno(tablero):
            imprimir_tablero(tablero)
            print("¡Empate!")
            break

        turno = "O" if turno == "X" else "X"

# Ejemplo de uso

print("1. Humano vs IA")
print("2. IA vs IA")
opcion = input("Elige el modo de juego (1 o 2): ")

if opcion == "1":
    jugador_humano = input("¿Con qué juega el humano? (X u O): ").upper()
    jugador_ia = "O" if jugador_humano == "X" else "X"
    jugar_humano_vs_ia(jugador_humano, jugador_ia)
elif opcion == "2":
    jugar_ia_vs_ia("X", "O")
else:
    print("Opción no válida.")