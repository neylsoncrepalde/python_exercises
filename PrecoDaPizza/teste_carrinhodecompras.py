#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 00:18:15 2018
Testes CarrinhoDeCompras
@author: neylson
"""

import unittest
from pizza import Pizza
from carrinhodecompras import CarrinhoDeCompras

class TesteCarrinhoDeCompras(unittest.TestCase):
    
    def setUp(self):
        self.pizza1 = Pizza()
        self.pizza1.adicionaIngrediente("Mussarela")
        self.pizza1.adicionaIngrediente("Molho")
        self.pizza1.adicionaIngrediente("Tomate")
        self.pizza1.adicionaIngrediente("Manjericão")
        
        self.pizza2 = Pizza()
        self.pizza2.adicionaIngrediente("Mussarela")
        self.pizza2.adicionaIngrediente("Provolone")
        self.pizza2.adicionaIngrediente("Parmesão")
        self.pizza2.adicionaIngrediente("Cheddar")
        self.pizza2.adicionaIngrediente("Molho")
        self.pizza2.adicionaIngrediente("Roquefort")
        
        self.pizza3 = Pizza()
        self.pizza3.adicionaIngrediente("Mussarela")
        
        self.carrinho = CarrinhoDeCompras()
        self.carrinho.adicionaPizza(self.pizza1)
        self.carrinho.adicionaPizza(self.pizza2)
        self.carrinho.adicionaPizza(self.pizza3)
        
    def test_somaPreco(self):
        self.assertEqual(self.carrinho.precoTotal, 58)
        
    def test_naoAceitaPizzaSemIngredientes(self):
        pizza4 = Pizza()
        self.assertRaises(ValueError, self.carrinho.adicionaPizza(pizza4))
    
if __name__ == '__main__':
    unittest.main()

    
    
    
    