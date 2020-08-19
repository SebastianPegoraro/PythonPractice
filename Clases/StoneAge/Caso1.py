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



    



