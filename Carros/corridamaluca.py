# Define a classe corrida e seus métodos

class CorridaMaluca:
    def __init__(self, tamanho):
        self.pista = tamanho
        self.carros = []
        self.dicionario = {}

    def adicionaCarro(self, carro):
        self.carros.append(carro)
        nome = str(carro.getNome())
        self.dicionario[nome] = 0
        #CorridaMaluca.dicionario.update(nome = 0)

    def terminou(self):
        for valor in self.dicionario.values():
            if valor >= self.pista:
                return True
        return False

    def umDoisTresEJa(self):
        
        while not self.terminou():
            for carro in self.carros:
                carro.acelerar()
                distancia = carro.getVelocidade()
                nome = str(carro.getNome())
                self.dicionario[nome] += distancia
                #CorridaMaluca.dicionario.update(nome = distancia)

        for carro, value in self.dicionario.items():
            print(carro + " - " + str(value))
