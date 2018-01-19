#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:21:52 2018
Classe CarrinhoDeCompras
@author: neylson
"""

class CarrinhoDeCompras:
    def __init__(self):
        self.precoTotal = 0
    
    def adicionaPizza(self, pizza):
        if pizza.ingredientes == {}:
            raise ValueError('A pizza deve ter pelo menos um ingrediente.')
        else:
            self.precoTotal += pizza.getPreco()