import pandas as pd

# Crear listas:
lista_1 = ['Ana', 'Juan', 'María']
print("Lista 1:",lista_1)
lista_2 = [350, 450, 'María']
print("Lista 2:",lista_2)
lista_3 = ['Ana', -3.1416, 'María']
print("Lista 3:",lista_3)

#Crear series a partir de las listas:
serie_1 = pd.Series(lista_1)
print("\nSerie 1:")
print(serie_1)
serie_2 = pd.Series(lista_2)
print("\nSerie 2:")
print(serie_2)
serie_3 = pd.Series(lista_3)
print("\nSerie 3:")
print(serie_3)


print( lista_2[1] )

serie_3 = pd.Series(['Ana', -3.1416, 'María'], index=[100, 200, 300])
print("\nSerie 3:")
print(serie_3)
