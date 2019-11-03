#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo faz a criação 
  de codificação Base64

  Modificado em 25 de janeiro de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Coloca a ms aqui
msg = raw_input('Coloque uma string para codificar: ')

# Printa na tela
print "Sua seqüência codificada em B64 é: " + msg.encode('base64')
