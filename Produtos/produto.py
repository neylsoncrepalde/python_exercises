# Exercício Programação Orientada a Objetos

class Produto:
    def __init__(self, nome, codigo, preco):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        
    def produtosIguais(self, produto2):
        if self.codigo == produto2.codigo:
            return True
        else:
            return False
