#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 15:06:52 2018
Testes ProdutoComTamanho
@author: neylson
"""
import unittest
from produtocomtamanho import ProdutoComTamanho

class TestesProdutoComTamanho(unittest.TestCase):
    
    def setUp(self):
        self.sapato1 = ProdutoComTamanho("Arezzo", 1, 150, 40)
        self.sapato2 = ProdutoComTamanho("Arezzo", 1, 150, 42)
        self.sapato3 = ProdutoComTamanho("Sergios", 2, 200, 40)
        self.sapato4 = ProdutoComTamanho("Outra Marca", 1, 100, 40)
        self.camisa = ProdutoComTamanho("CiaTerno", 3, 50, 40)
        
    def test_ProdutosComTamanhoIguais(self):
        self.assertTrue(self.sapato1.produtoComTamanhoIguais(self.sapato4))
        self.assertFalse(self.sapato1.produtoComTamanhoIguais(self.sapato2))
        self.assertFalse(self.sapato1.produtoComTamanhoIguais(self.sapato3))
        self.assertFalse(self.sapato1.produtoComTamanhoIguais(self.camisa))
        
if __name__ == "__main__":
    unittest.main()