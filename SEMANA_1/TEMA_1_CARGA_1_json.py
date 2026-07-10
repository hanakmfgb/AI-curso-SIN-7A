# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 17:45:17 2025

@author: MARCELOFGB
"""

import pandas as pd
# Supongamos 'datos.json' con:
'''
[{"Nombre": "Juan", "Edad": 30, "Ciudad": "Madrid"},
 {"Nombre": "Maria", "Edad": 25, "Ciudad": "Barcelona"},
 {"Nombre": "Pedro", "Edad": 40, "Ciudad": "Valencia"}]
'''
df = pd.read_json('datos.json', orient='records')
print(df)

