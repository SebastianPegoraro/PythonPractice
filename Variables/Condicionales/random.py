#Solicite al usuario el ingreso de 3 números, e imprímalos de mayor a menor.
valor1 = input("Ingresa el primer valor \n")
valor2 = input("Ingresa el segundo valor \n")
valor3 = input("Ingresa el tercero valor \n")

if valor1 > valor2 and valor1 > valor3:
    print( valor1 )
    if valor2 > valor3:
        print( valor2 )
        print( valor3 )
    else:
        print( valor3 )
        print( valor2 )

if valor2 > valor1 and valor2 > valor3:
    print( valor2 )
    if valor1 > valor3:
        print( valor1 )
        print( valor3 )
    else:
        print( valor3 )
        print( valor1 )

if valor3 > valor1 and valor2 < valor3:
    print( valor3 )
    if valor1 > valor2:
        print( valor1 )
        print( valor2 )
    else:
        print( valor2 )
        print( valor1 )
