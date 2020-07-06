#Elabore un programa que dada una lista de 15 elementos, copie en otra lista los elementos pares multiplicados por 2.
import random
lista = []
for indice in range(0, 15):
    lista.append(random.randint(0, 50))

print(lista)
otra_lista = []

for valor in lista:
    if valor % 2 == 0 and valor != 0:
        otra_lista.append(valor * 2)

print(otra_lista)



