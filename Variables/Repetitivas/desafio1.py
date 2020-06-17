#Determinar el número mayor de 10 números ingresados.
import random

lista = []
for index in range(10):
    lista.append(random.randint(0,500))

for index in range(0,len(lista)):
    print(lista[index])

mayor = 0
for index in range(0,len(lista)):
    if lista[index] > mayor:
        mayor = lista[index]

print()
print("El numero mayor es: " + str(mayor))