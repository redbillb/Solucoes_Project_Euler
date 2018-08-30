# -*- coding: utf-8 -*-

#imports
import unittest
from math import sqrt

def verificaIntegridadeDosParametros(num_a,num_b,num_c):
	if num_a < num_b and num_b < num_c:
		return True
	return False

def verificaSomaParametros(num_a,num_b,num_c):
	if num_a + num_b + num_c == 1000:
		return True
	return False

def calculaParametroC(num_a,num_b):
	return sqrt(num_a * num_a + num_b * num_b)

def encontraTrioPitagorico():
	for num1 in range(1000+1):
		for num2 in range(1000+1):
			num3 = calculaParametroC(num1,num2)
			if verificaSomaParametros(num1,num2,num3) and verificaIntegridadeDosParametros(num1,num2,num3):
				return num1*num2*num3


class TestaTripePitagorigo(unittest.TestCase):
	def testaverificaIntegridadeDosParametros(self):
		self.assertTrue(verificaIntegridadeDosParametros(3,4,5))
		self.assertFalse(verificaIntegridadeDosParametros(3,5,4))

	def testaVerificaSomaParametros(self):
		self.assertTrue(verificaSomaParametros(200,300,500))
		self.assertFalse(verificaSomaParametros(200,300,600))

	def testaCalculaParametroC(self):
		self.assertEqual(5,calculaParametroC(3,4))
		self.assertNotEqual(5,calculaParametroC(3,5))

		print (encontraTrioPitagorico())


if __name__ == '__main__':
	unittest.main()
