# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 20:13:55 2026

@author: MARCELOFGB
"""
import pandas as pd
# Crear dataset de Ventas
data_ventas = {
    'Vendedor': ['Juan', 'Maria', 'Juan', 'Maria', 'Pedro', 'Juan'],
    'Producto': ['Tablet', 'Tablet', 'Laptop', 'Laptop', 'Tablet', 'Monitor'],
    'Monto': [200, 220, 1000, 1100, 210, 300],
    'Fecha': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', '2023-01-01', '2023-01-04'])
}



df_ventas = pd.DataFrame(data_ventas)


# 1. GroupBy: ¿Cuánto vendió cada vendedor en total?
ventas_por_vendedor = df_ventas.groupby('Vendedor')['Monto'].sum().sort_values(ascending=False)
print("--- Ventas Totales por Vendedor ---")
print(ventas_por_vendedor)

# 2. Pivot Table: Matriz de Vendedor vs Producto
tabla_pivote = df_ventas.pivot_table(values='Monto', index='Vendedor', columns='Producto', aggfunc='sum', fill_value=0)
print("\n--- Tabla Pivote (Vendedor vs Producto) ---")
print(tabla_pivote)