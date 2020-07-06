"""
Dados los datos de un municipio: zona, sexo y edad de cada uno de sus habitantes, encontrar:

a) porcentaje de varones menores de 15 años para cada zona

b) porcentaje de varones menores de 15 años para todo el municipio

Los datos vienen ordenados por zona.Con dato de zona igual a 0, se indica el fin.
"""
import random

contador_persona=0
contador_varon_menor=0
for i in range(0, 10):
    contador_varon_menor_zona=0
    contador_persona_zona=0
    condicion= True
    while condicion:
        contador_persona +=1
        contador_persona_zona +=1
        print("Ingrese sexo: \n 1- Mujer \n 2- Varon")
        sexo = random.randint(0,2)
        if sexo == 2:
            print("Ingrese edad:")
            edad = random.randint(0,80)
            if edad < 15:
                contador_varon_menor+=1
                contador_varon_menor_zona+=1
        
        if random.randint(-1, 10) == 0:
            condicion = False
    
    porcentaje_zona = (contador_varon_menor_zona * 100) / contador_persona_zona
    print("Porcentaje de varones menores: \n Zona => ",i," \n Porcentaje => %",porcentaje_zona)

porcentaje = (contador_varon_menor * 100) / contador_persona
print("Porcentaje de varones menores: \n Porcentaje => %",porcentaje)

                

            

