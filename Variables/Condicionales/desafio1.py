#Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad distinta. 
#Obtener el porcentaje que cada quien invierte con respecto a la cantidad total invertida.

primera_inversion = float(input("Ingrese la primera inversion \n"))
segunda_inversion = float(input("Ingrese la segunda inversion \n"))
tercera_inversion = float(input("Ingrese la tercera inversion \n"))

total_invertido =primera_inversion+segunda_inversion+tercera_inversion

print("EL porcentaje es de: " + str(primera_inversion*100/total_invertido))
print("EL porcentaje es de: " + str(segunda_inversion*100/total_invertido))
print("EL porcentaje es de: " + str(tercera_inversion*100/total_invertido))
