# Classe ProdutoComTamanho

from produto import Produto

class ProdutoComTamanho(Produto):
    def __init__(self, nome, codigo, preco, tamanho):
        Produto.__init__(self, nome, codigo, preco)
        self.tamanho = tamanho
        
