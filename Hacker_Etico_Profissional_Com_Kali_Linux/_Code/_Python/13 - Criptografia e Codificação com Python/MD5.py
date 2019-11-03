#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo cria uma 
  hash MD5

  Modificado em 24 de janeiro de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Importa as bibliotecas necessárias
import hashlib

message = raw_input("Digite a seqüência de caracteres para trasnformar em hash: ")
md5 = hashlib.md5(message.encode()) # Faz a conversão da mensagem em MD5

print (md5.hexdigest())  # printa em hash md5 




