# -*- coding: utf-8 -*-

#imports
import unittest
from math import sqrt

primos = [2,]

def encontraPrimosESoma(limite):   
    primos = [2,]
    for numero in range(3,limite+1,2):
        ehprimo = 1
        for i in primos:
            if numero % i == 0:
                ehprimo = 0
                break
            if i > sqrt(numero):
                break
        if (ehprimo):
            primos.append(numero)
    return sum(primos)

class TestaPrimos(unittest.TestCase):

    def testeEncontraPrimosESoma(self):
        self.assertEqual(17,encontraPrimosESoma(10))
        self.assertEqual(142913828922,encontraPrimosESoma(2000000))

if __name__ == '__main__':
    unittest.main()
