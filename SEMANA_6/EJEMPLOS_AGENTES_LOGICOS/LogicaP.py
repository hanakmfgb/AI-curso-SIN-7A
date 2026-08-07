# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 19:51:18 2025

@author: MARCELOFGB
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class DiagnosticoAutomovil:
    def __init__(self, root):
        self.root = root
        self.root.title("Diagnóstico de Fallas del Automóvil")

        # Variables de control (checkboxes)
        self.bateria_var = tk.BooleanVar()
        self.ruido_var = tk.BooleanVar()
        self.luces_var = tk.BooleanVar()

        # Interfaz gráfica
        ttk.Label(root, text="Síntomas:").grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Checkbutton(root, text="Batería descargada", variable=self.bateria_var).grid(row=1, column=0, sticky=tk.W, padx=10)
        ttk.Checkbutton(root, text="Motor de arranque hace ruido", variable=self.ruido_var).grid(row=2, column=0, sticky=tk.W, padx=10)
        ttk.Checkbutton(root, text="Las luces no encienden", variable=self.luces_var).grid(row=3, column=0, sticky=tk.W, padx=10)

        ttk.Button(root, text="Diagnosticar", command=self.diagnosticar).grid(row=4, column=0, columnspan=2, pady=20)

    def diagnosticar(self):
        # Obtener las observaciones del usuario
        bateria = self.bateria_var.get()
        ruido = self.ruido_var.get()
        luces = self.luces_var.get()

        # Aplicar la lógica proposicional (inferencia)
        no_arranca = False
        if bateria and not luces:
           no_arranca = True
        if ruido:
           no_arranca = True

        if no_arranca:
            messagebox.showinfo("Diagnóstico", "El automóvil probablemente NO arranca.")
        else:
            messagebox.showinfo("Diagnóstico", "No se puede determinar si el automóvil arranca con los síntomas proporcionados.")


if __name__ == "__main__":
    root = tk.Tk()
    app = DiagnosticoAutomovil(root)
    root.mainloop()