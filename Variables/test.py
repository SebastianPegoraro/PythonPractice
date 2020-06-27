numero = int(input("Cuantas notas quieres ingresar"))
sumatoria = 0
contador = numero
while contador > 0:
    nota = int(input("Ingrese la nota"))
    sumatoria = sumatoria + nota
    contador -= 1

print("El promedio de las notas es ", sumatoria/numero)