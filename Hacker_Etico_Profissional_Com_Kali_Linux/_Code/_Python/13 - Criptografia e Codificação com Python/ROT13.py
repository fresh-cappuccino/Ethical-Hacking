#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo faz a criação 
  de codificação ROT13

  Modificado em 24 de janeiro de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Importação das bibliotecas necessárias
from string import maketrans, lowercase, uppercase

# Função que faz a conversão da string em ROT13
def rot13(message):
	lower = maketrans(lowercase, lowercase[13:] + lowercase[:13])
	upper = maketrans(uppercase, uppercase[13:] + uppercase[:13])
	return message.translate(lower).translate(upper)

# Variavél para fazer a conversão
message = raw_input('Enter :')

# Printa na tela o seu resultado
print rot13(message)
