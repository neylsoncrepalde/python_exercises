#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 22:15:09 2018
Testes Pizza
@author: neylson
"""
import unittest
from pizza import Pizza

class TestPizza(unittest.TestCase):
    
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
        
    def tearDown(self):
        Pizza.zeraListaDeIngredientes()
    
    def test_valorCorreto4(self):
        self.assertEqual(self.pizza1.getPreco(), 20)

    def test_valorCorreto1(self):
        self.assertEqual(self.pizza3.getPreco(), 15)
        
    def test_valorCorreto6(self):
        self.assertEqual(self.pizza2.getPreco(), 23)
        
    def test_registroIngredientes(self):
        self.assertListEqual(self.pizza1.ingredientes, ["Mussarela", "Molho",
                                                   "Tomate", 
                                                   "Manjericão"])
        self.assertDictEqual(Pizza.ingredientes, {'Cheddar': 1,
                                                 'Manjericão': 1,
                                                 'Molho': 2,
                                                 'Mussarela': 3,
                                                 'Parmesão': 1,
                                                 'Provolone': 1,
                                                 'Roquefort': 1,
                                                 'Tomate': 1})

    
if __name__ == '__main__':
    unittest.main()
