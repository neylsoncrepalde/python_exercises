# Define a classe CarroSoma como subclasse de CarroDeCorrida

from carrodecorrida import CarroDeCorrida

class CarroSoma(CarroDeCorrida):
    def __init__(self, nome, velocidadeMaxima, potencia):
        CarroDeCorrida.__init__(self, nome, velocidadeMaxima)
        self.potencia = potencia
        print("(Inicializa CarroSoma)")

    def acelerar(self):
        self.velocidade += self.potencia
        if self.velocidade > self.velocidadeMaxima:
            self.velocidade = self.velocidadeMaxima


