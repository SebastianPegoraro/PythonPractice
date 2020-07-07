
def lista_personas(ruta):    
    personas = []

    with open(ruta , encoding='utf8') as fichero:
        for linea in fichero:
            lista = linea.split(';', 1)
            diccionario={}
            diccionario.setdefault(lista[0], lista[1])
            personas.append(diccionario)

    return personas

def mostrar_persona(persona):
    nombre,apellido,nacimiento = persona.split(';')        
    return nombre,apellido,nacimiento


path = 'Ficheros\Datos\personas.txt'

personas = lista_personas(path)

for diccionario in personas:
    for key in diccionario:
        nombre,apellido,nacimiento = mostrar_persona(diccionario[key])
        print("El usuario ",apellido,nombre," nacio el: ",nacimiento)