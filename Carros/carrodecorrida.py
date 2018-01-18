# Define a superclasse CarroDeCorrida

class CarroDeCorrida:
    def __init__(self, nome, velocidadeMaxima):
        self.velocidade = 0
        self.velocidadeMaxima = velocidadeMaxima
        self.nome = nome
        print("(Inicializando CarroDeCorrida)")
    
    def acelerar(self):
        pass

    def frear(self):
        self.velocidade = self.velocidade/2

    def getVelocidade(self):
        return self.velocidade

    def getNome(self):
        return self.nome

    
