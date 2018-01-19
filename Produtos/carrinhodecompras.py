# Classe CarrinhoDeCompras
# Falta implementar produtos com tamanhos diferentes
# serão considerados diferentes

class CarrinhoDeCompras:
    def __init__(self):
        self.items = []
        self.quantidades = {}

    def adicionaProduto(self, produto, quantidade):
        if produto not in self.items:
            self.items.append(produto)
        
        if produto.nome not in self.quantidades:
            self.quantidades[produto.nome] = {"quantidade": 0,
                                              "preco": produto.preco}
            self.quantidades[produto.nome]["quantidade"] += quantidade
        else:
            jatem = [item.produtoComTamanhoIguais(produto) for \
                     item in self.items]
            if True in jatem:
                self.quantidades[produto.nome]["quantidade"] += quantidade
            else:
                self.quantidades[produto.nome] = {"quantidade": quantidade,
                                                  "preco": produto.preco}
        
    def removeProduto(self, produto, quantidade):
        if produto not in self.items:
            raise ValueError("Não há um item deste produto no carrinho.")
        else:
            jatem = [item.produtoComTamanhoIguais(produto) for \
                     item in self.items]
            if True in jatem:
                self.quantidades[produto.nome]["quantidade"] -= quantidade
    
    # Calcula o valor da compra
    def calculaValorCompra(self):
        valorTotal = 0
        for item in self.quantidades.keys:
            valorParcial = item["quantidade"] * item["preco"]
            valorTotal += valorParcial
        
    
    