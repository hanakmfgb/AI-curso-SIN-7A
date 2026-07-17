# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 21:53:40 2025

@author: MARCELOFGB
"""

import pygame
import random

# --- Configuración ---
ANCHO = 800
ALTO = 600
FPS = 30
CARRETERA_ANCHO = 200
CARRIL_ANCHO = CARRETERA_ANCHO // 3
NUM_CARRILES = 3
DISTANCIA_SEGURA = 25  # Distancia mínima entre coches
VELOCIDAD_MAXIMA = 5
VELOCIDAD_MINIMA = 2
COLOR_FONDO = (50, 50, 50)
COLOR_CARRETERA = (100, 100, 100)
COLOR_LINEA_CARRIL = (255, 255, 255)
COLOR_COCHE = (255, 30, 0)
COLOR_COCHE_AGENTE = (0, 50, 0)  # Coche controlado por el agente

# --- Clases ---
class Coche(pygame.sprite.Sprite):
    def __init__(self, carril, y, velocidad, es_agente=False):
        super().__init__()
        self.image = pygame.Surface((40, 20))
        self.image.fill(COLOR_COCHE_AGENTE if es_agente else COLOR_COCHE) # Distingue visualmente el coche del agente
        self.rect = self.image.get_rect()
        self.carril = carril
        self.rect.center = (ANCHO // 2 - CARRETERA_ANCHO // 2 + carril * CARRIL_ANCHO + CARRIL_ANCHO // 2, y)
        self.velocidad = velocidad
        self.es_agente = es_agente
        self.longitud = 40  # Longitud del coche para la detección de colisiones

    def update(self):
        self.rect.y += self.velocidad
        if self.rect.bottom > ALTO:
            self.rect.top = 0 - self.longitud  # Reaparece arriba
            self.carril = random.randint(0, NUM_CARRILES - 1)
            self.rect.centerx = ANCHO // 2 - CARRETERA_ANCHO // 2 + self.carril * CARRIL_ANCHO + CARRIL_ANCHO // 2
            self.velocidad = random.randint(VELOCIDAD_MINIMA, VELOCIDAD_MAXIMA)

    def frenar(self, factor=0.5):
        self.velocidad *= factor
        self.velocidad = max(self.velocidad, VELOCIDAD_MINIMA) # No puede frenar por debajo de VELOCIDAD_MINIMA

    def acelerar(self, factor=1.2):
         self.velocidad *= factor
         self.velocidad = min(self.velocidad, VELOCIDAD_MAXIMA) # No puede acelerar por encima de VELOCIDAD_MAXIMA

    def cambiar_carril(self, direccion): # dirección puede ser 1 (derecha) o -1 (izquierda)
        nuevo_carril = self.carril + direccion
        if 0 <= nuevo_carril < NUM_CARRILES:
            self.carril = nuevo_carril
            self.rect.centerx = ANCHO // 2 - CARRETERA_ANCHO // 2 + self.carril * CARRIL_ANCHO + CARRIL_ANCHO // 2

class Trafico:
    def __init__(self):
        self.coches = pygame.sprite.Group()
        self.coche_agente = Coche(1, ALTO // 2, 3, True) # El agente empieza en el carril del medio
        self.coches.add(self.coche_agente)

        # Generar algunos coches iniciales
        for _ in range(10):
            carril = random.randint(0, NUM_CARRILES - 1)
            y = random.randint(-ALTO, 0)
            velocidad = random.randint(VELOCIDAD_MINIMA, VELOCIDAD_MAXIMA)
            coche = Coche(carril, y, velocidad)
            self.coches.add(coche)


    def actualizar(self):
        self.coches.update()
        self.controlar_agente()
        self.evitar_colisiones()

    def dibujar(self, pantalla):
        pantalla.fill(COLOR_FONDO)
        # Dibujar la carretera
        pygame.draw.rect(pantalla, COLOR_CARRETERA, (ANCHO // 2 - CARRETERA_ANCHO // 2, 0, CARRETERA_ANCHO, ALTO))
        # Dibujar las líneas de los carriles
        for i in range(1, NUM_CARRILES):
            x = ANCHO // 2 - CARRETERA_ANCHO // 2 + i * CARRIL_ANCHO
            pygame.draw.line(pantalla, COLOR_LINEA_CARRIL, (x, 0), (x, ALTO), 2)

        self.coches.draw(pantalla)

    def detectar_coche_delante(self, coche):
        """Detecta el coche más cercano delante del coche dado en el mismo carril.
           Retorna None si no hay coche delante.
        """
        coche_delante = None
        distancia_minima = float('inf')  # Distancia infinita

        for otro_coche in self.coches:
            if otro_coche != coche and otro_coche.carril == coche.carril and otro_coche.rect.y > coche.rect.y:
                distancia = otro_coche.rect.y - coche.rect.y
                if distancia < distancia_minima:
                    distancia_minima = distancia
                    coche_delante = otro_coche

        return coche_delante

    def controlar_agente(self):
        """Controla el coche del agente para evitar colisiones."""
        coche_delante = self.detectar_coche_delante(self.coche_agente)

        if coche_delante:
            distancia = coche_delante.rect.y - self.coche_agente.rect.y
            if distancia < DISTANCIA_SEGURA:
                self.coche_agente.frenar() # El agente frena para mantener la distancia segura.
            else:
                self.coche_agente.acelerar() # Acelera si la distancia es segura.
        else:
            self.coche_agente.acelerar() # Si no hay coche delante acelera.


    def evitar_colisiones(self):
        """Evita colisiones entre todos los coches (incluido el del agente)."""
        for coche in self.coches:
            if coche == self.coche_agente:
               continue # No queremos que el agente reaccione a sí mismo.

            coche_delante = self.detectar_coche_delante(coche)

            if coche_delante:
                distancia = coche_delante.rect.y - coche.rect.y
                if distancia < DISTANCIA_SEGURA:
                    coche.frenar()  # El coche frena para evitar la colisión.
                else:
                    coche.acelerar() # Acelera si la distancia es segura.
            else:
                coche.acelerar() # Si no hay coche delante, acelera.

# --- Inicialización ---
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Simulación de Tráfico con Agente Inteligente")
reloj = pygame.time.Clock()

trafico = Trafico()

# --- Bucle Principal ---
ejecutando = True
while ejecutando:
    # --- Manejo de Eventos ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:  # Agregar control manual del agente
            if evento.key == pygame.K_LEFT:
                trafico.coche_agente.cambiar_carril(-1) # Mover a la izquierda
            if evento.key == pygame.K_RIGHT:
                trafico.coche_agente.cambiar_carril(1) # Mover a la derecha


    # --- Actualización ---
    trafico.actualizar()

    # --- Dibujo ---
    trafico.dibujar(pantalla)
    pygame.display.flip()

    # --- Control de FPS ---
    reloj.tick(FPS)

# --- Finalización ---
pygame.quit()