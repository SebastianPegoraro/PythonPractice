txt = "hello, my name is Peter, I am 26 years old"

minusculas = txt.lower()

x = minusculas.split(", ")

cont = 0
for palabla in x:
    for caracter in palabla:
        if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
            cont += 1
        #print(caracter,)
    
    print(palabla," => ", cont)

#print(x)