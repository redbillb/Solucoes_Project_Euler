# -*- coding: utf-8 -*-

#imports
import unittest

def calculaElementoSequencia(numero):
	resultado = 0
	for num in range(1,numero + 1):
		resultado += num
	return resultado

def encontraDivisores(numero):
	lista = []
	for num in range(1,int((numero + 2) / 2)):
		if numero % num == 0:
			lista.append(num)
	lista.append(numero)
	return lista

def processa(quantidadeDivisores):
	numero = 1
	while True:
		res = calculaElementoSequencia(numero)
		divisores = encontraDivisores(res)
		if len(divisores) >= quantidadeDivisores:
			break
		numero += 1
		print (f'numero:{numero}  quantidade divisores:{len(divisores)}')
	return res


class TestaProcessaDivisores(unittest.TestCase):
	def testaCalculaElementoSeuquencia(self):
		self.assertEqual(1,calculaElementoSequencia(1))
		self.assertEqual(3,calculaElementoSequencia(2))
		self.assertEqual(6,calculaElementoSequencia(3))
		self.assertEqual(10,calculaElementoSequencia(4))
		self.assertEqual(15,calculaElementoSequencia(5))
		self.assertEqual(21,calculaElementoSequencia(6))
		self.assertEqual(28,calculaElementoSequencia(7))

	def testaEncontraDivisores(self):
		self.assertEqual([1],encontraDivisores(1))
		self.assertEqual([1,3],encontraDivisores(3))
		self.assertEqual([1,2,3,6],encontraDivisores(6))
		self.assertEqual([1,2,5,10],encontraDivisores(10))
		self.assertEqual([1,3,5,15],encontraDivisores(15))
		self.assertEqual([1,2,4,7,14,28],encontraDivisores(28))

	def testaProcessa(self):
		self.assertEqual(28,processa(6))

	print (processa(500))

if __name__ == '__main__':
	unittest.main()
