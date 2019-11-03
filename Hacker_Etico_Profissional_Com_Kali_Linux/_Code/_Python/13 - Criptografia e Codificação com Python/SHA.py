#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo cria uma 
  hash SHA1, SHA256 e em SHA 512

  Modificado em 24 de janeiro de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""
import sys

# Tentativa de importação das bibliotecas necessárias
import hashlib

# Funções de SHA
def SHA1():
	message = raw_input("Escreva uma string para hash SHA1: ")
	sha = hashlib.sha1(message)
	sha1 = sha.hexdigest()
	print sha1 # Printa na tela os resultados 

def SHA256():
	message = raw_input("Escreva uma string para hash SHA256: ")
	sha = hashlib.sha256(message)
	sha256 = sha.hexdigest()
	print sha256 # Printa na tela os resultados 

def SHA512():
	message = raw_input("Escreva uma string para hash SHA512: ")
	sha = hashlib.sha512(message)
	sha512 = sha.hexdigest()
	print sha512 # Printa na tela os resultados 

# Função principal
def main():
	# Chama as funções
	SHA1()
	SHA256()
	SHA512()

# main
if __name__ == '__main__':
	main()




