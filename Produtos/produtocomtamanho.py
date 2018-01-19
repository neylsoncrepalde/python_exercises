# Classe ProdutoComTamanho

from produto import Produto

class ProdutoComTamanho(Produto):
    def __init__(self, nome, codigo, preco, tamanho):
        Produto.__init__(self, nome, codigo, preco)
        self.tamanho = tamanho
        
    def produtoComTamanhoIguais(self, produto2):
        if self.produtosIguais(produto2):
            if self.tamanho == produto2.tamanho:
                return True
        else:
            return False
