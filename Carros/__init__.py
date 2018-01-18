# Faz a corrida acontecer

import os
#os.chdir('/home/neylson/python_exercises/Carros')
print(os.getcwd())

from corridamaluca import CorridaMaluca
from carrosoma import CarroSoma
from carromulti import CarroMulti

corrida = CorridaMaluca(2000)
corrida.adicionaCarro(CarroSoma("CarroA", 100, 10))
corrida.adicionaCarro(CarroSoma("CarroB", 140, 8))
corrida.adicionaCarro(CarroMulti("CarroC", 100, 1.7))
corrida.adicionaCarro(CarroMulti("CarroD", 110, 1.4))

print("\n")
corrida.umDoisTresEJa()
