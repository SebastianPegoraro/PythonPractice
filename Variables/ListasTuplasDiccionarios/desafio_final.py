"""
Se tiene una lista que almacena pedidos en orden de llegada, por ende puede haber más de un pedido para el mismo artículo. 
Crear una lista donde se almacene la cantidad de pedidos por artículo.
"""
import random

lista = []
for indice in range(0, 15):
    lista.append(0)

print(lista)
for indice in range(0,5):
    while True:
        articulo = random.randint(0,14)
        lista[articulo] += 1
        if random.randint(0, 5) == 0:
            break

print(lista)
