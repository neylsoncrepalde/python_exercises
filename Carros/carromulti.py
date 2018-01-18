# Define a classe CarroMulti como subclasse de CarroDeCorrida

from carrodecorrida import CarroDeCorrida

class CarroMulti(CarroDeCorrida):
    def __init__(self, nome, velocidadeMaxima, potencia):
        CarroDeCorrida.__init__(self, nome, velocidadeMaxima)
        if potencia < 1 and potencia > 2:
            self.potencia = 1.5
        else:
            self.potencia = potencia
        print("(Inicializa CarroMulti)")

    def acelerar(self):
        if self.velocidade == 0:
            self.velocidade = 10
        else:
            self.velocidade *= self.potencia
            if self.velocidade > self.velocidadeMaxima:
                self.velocidade = self.velocidadeMaxima
    
        
