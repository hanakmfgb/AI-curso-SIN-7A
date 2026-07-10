# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 12:34:08 2025

@author: MARCELOFGB
"""

import pandas as pd

#Uso de parámetros en la carga
df = pd.read_csv(filepath_or_buffer='Air_Quality.csv',  
                 index_col='Unique ID', 
                 sep=',',
                 header='infer')
print(df)



