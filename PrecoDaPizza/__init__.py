#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:30:37 2018
__init__
@author: neylson
"""

from carrinhodecompras import CarrinhoDeCompras
from pizza import Pizza

# Cria 3 pizzas
pizza1 = Pizza()
pizza2 = Pizza()
pizza3 = Pizza()

# Adiciona ingredientes
pizza1.adicionaIngrediente("Mussarela")
pizza1.adicionaIngrediente("Molho")
pizza1.adicionaIngrediente("Tomate")
pizza1.adicionaIngrediente("Manjericão")

pizza2.adicionaIngrediente("Mussarela")
pizza2.adicionaIngrediente("Provolone")
pizza2.adicionaIngrediente("Parmesão")
pizza2.adicionaIngrediente("Cheddar")
pizza2.adicionaIngrediente("Molho")
pizza2.adicionaIngrediente("Roquefort")

pizza3.adicionaIngrediente("Mussarela")

# Adiciona as pizzas em um carrinho de compras
carrinho = CarrinhoDeCompras()
carrinho.adicionaPizza(pizza1)
carrinho.adicionaPizza(pizza2)
carrinho.adicionaPizza(pizza3)

# Imprime o total do carrinho
print("O total do carrinho de compras foi de R$ " + 
      str(carrinho.precoTotal) + ",00 reais.")

# Imprime a quantidade utilizada de cada ingrediente
print("A quantidade utilizada de cada ingrediente:")
for key, value in Pizza.ingredientes.items():
    print(str(key) + " - " + str(value))
