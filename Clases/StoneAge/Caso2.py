class Vehiculo(object):
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def getColor(self):
        return self.color

    def getRuedas(self):
        return self.ruedas
        

class Coche(Vehiculo):
    def __init__(self, velocidad, cilindrada, color, ruedas):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def getVelocidad(self):
        return self.velocidad

    def getCilindrada(self):
        return self.cilindrada


class Camioneta(Coche):
    def __init__(self, velocidad, cilindrada, color, ruedas, carga):
        Coche.__init__(self, velocidad, cilindrada, color, ruedas)
        self.carga = carga

    def getCarga(self):
        return self.carga


class Bicicleta(Vehiculo):
    def __init__(self, tipo, color, ruedas):
        Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo

    def getTipo(self):
        return self.tipo


class Motocicleta(Bicicleta):
    def __init__(self, velocidad, cilindrada, tipo, color, ruedas):
        Bicicleta.__init__(self, color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def getVelocidad(self):
        return self.velocidad

    def getCilindrada(self):
        return self.cilindrada


vwgol = Coche("120km", "2.0cc", "azul", 4)
sandero = Camioneta("120km", "2.0cc", "azul", 4, "200kg")
mountainbike = Camioneta("120km", "2.0cc", "azul", 4, "200kg")
sandero = Camioneta("120km", "2.0cc", "azul", 4, "200kg")
