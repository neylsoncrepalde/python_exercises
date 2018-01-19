# Classe CarrinhoDeCompras
# Falta implementar produtos com tamanhos diferentes
# serão considerados diferentes

from produtocomtamanho import ProdutoComTamanho

class CarrinhoDeCompras:
    def __init__(self):
        self.items = []
        self.quantidades = {}

    def adicionaProduto(self, produto, quantidade):
        self.items.append(produto)
        if produto.nome not in self.quantidades:
            self.quantidades[produto.nome] = 0
            self.quantidades[produto.nome] += quantidade
        else:
            self.quantidades[produto.nome] += quantidade
            
    # Continuar implementando removeProduto
