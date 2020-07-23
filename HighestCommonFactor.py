"""
Escriba una función que tome dos enteros positivos que representan el numerador y el denominador de una fracción como sus dos únicos parámetros. 
El cuerpo de la función debe reducir la fracción a los términos más bajos y luego devolver el numerador y el denominador de la fracción reducida como resultado. 
Por ejemplo, si los parámetros pasados ​​a la función son 6 y 63, las funciones deberían volver 2 y 21. 
Incluya un programa principal que permita al usuario ingresar un numerador y un denominador. 
Entonces su programa debería mostrar la fracción reducida.
"""

def compute_hcf(number1, number2):
    if number1 > number2:
        smaller = number2
    else:
        smaller = number1
    
    hcf=1

    for i in range(1, smaller+1):
        if((number1 % i == 0) and (number2 % i == 0)):
            hcf = i 
    return hcf


numerador = int(input("Ingrese el numerador \n"))
denominador = int(input("Ingrese el denominador \n"))

hcf = compute_hcf(numerador, denominador)

numeradorReducido = numerador / hcf
denominadorReducido = denominador / hcf

print("La fraccion es: \n" , numerador ,"/", denominador ,"\n Y la fraccion reducida es: \n", numeradorReducido , "/" , denominadorReducido)

