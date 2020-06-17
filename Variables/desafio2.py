tamanio = float(input("Ingrese el tamaño del pez \n"))
if tamanio >= 10:
    print("Pez contaminado")
elif tamanio >= 7:
    print("Pez con síntomas de organismo contaminado")
elif tamanio >= 4:
    print("Pez en buenas condiciones")
else:
    print("Pez con problemas de nutrición")

input()