#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
condicion = True
lista = []
while condicion:
    asignatura = input("Ingrese la Asignatura \n")
    lista.append(asignatura)

    respuesta = input("Ingresar otra asignatura? \n 0-Si \n Otro-No \n")
    if int(respuesta) != 0:
        condicion = False

print(lista)
