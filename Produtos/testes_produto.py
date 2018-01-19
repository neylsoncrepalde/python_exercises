#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 15:00:41 2018
Testes Produto
@author: neylson
"""
import unittest
from produto import Produto

class TestesProduto(unittest.TestCase):
    
    def setUp(self):
        self.sabonete = Produto("Dove", 1, 5)
        self.lapis = Produto("Lápis", 2, 1)
        self.caneta = Produto("Bic", 3, 2)
        self.tinteiro = Produto("Tinteiro", 3, 200)
        
    def test_produtosIguais(self):
        self.assertTrue(self.caneta.produtosIguais(self.tinteiro))
        self.assertFalse(self.caneta.produtosIguais(self.sabonete))

if __name__ == "__main__":
    unittest.main()