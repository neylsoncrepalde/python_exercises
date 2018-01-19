#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:08:48 2018
Classe Piza
@author: neylson
"""

class Pizza:
    
    ingredientes = {}
    
    def __init__(self):
        self.ingredientes = []
        pass
    
    def __contabilizaIngrediente(self, ingrediente):
        if ingrediente not in Pizza.ingredientes:
            Pizza.ingredientes[ingrediente] = 0
            Pizza.ingredientes[ingrediente] += 1
        else:
            Pizza.ingredientes[ingrediente] += 1
    
    def adicionaIngrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)
        self.__contabilizaIngrediente(ingrediente)
        
    def getPreco(self):
        if len(self.ingredientes) <= 2:
            return 15
        elif len(self.ingredientes) > 2 and len(self.ingredientes) <= 5:
            return 20
        elif len(self.ingredientes) > 5:
            return 23
    
    @classmethod
    def zeraListaDeIngredientes(cls):
        cls.ingredientes = {}