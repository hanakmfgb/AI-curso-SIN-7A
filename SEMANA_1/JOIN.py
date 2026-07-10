# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 20:15:50 2026

@author: MARCELOFGB
"""
import pandas as pd
# DataFrame de Empleados
df_emp = pd.DataFrame({
    'Emp_ID': [101, 102, 103, 104],
    'Nombre': ['Alicia', 'Beto', 'Carla', 'David'],
    'Dept_ID': [1, 2, 1, 3] # David está en un depto (3) que no existe en la tabla de abajo
})

# DataFrame de Departamentos
df_dept = pd.DataFrame({
    'Dept_ID': [1, 2, 4], # El depto 4 no tiene empleados
    'Departamento': ['RRHH', 'Finanzas', 'IT']
})

# 1. Inner Join (Solo coincidencias)
inner_join = pd.merge(df_emp, df_dept, on='Dept_ID', how='inner')
print("--- Inner Join (Solo coincidencias) ---")
print(inner_join)

# 2. Left Join (Todos los empleados, tengan o no depto)
left_join = pd.merge(df_emp, df_dept, on='Dept_ID', how='left')
print("\n--- Left Join (Todos los empleados) ---")
print(left_join)