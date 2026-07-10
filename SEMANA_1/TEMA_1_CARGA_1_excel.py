# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 12:34:08 2025

@author: MARCELOFGB
"""

import pandas as pd

# Supongamos que tenemos un archivo Excel 'datos.xlsx' con una hoja llamada 'Hoja1'
# instalar openpyxl
df = pd.read_excel('datos.xlsx', sheet_name='Hoja1') # o sheet_name=0
print(df)

