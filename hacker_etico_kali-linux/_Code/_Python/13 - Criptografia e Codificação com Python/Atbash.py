#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo faz a descoberta de 
  cifras de substituição para ASCII 

  Modificado em 26 de janeiro de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Bilbiotecas importadas
import string

input = raw_input("Coloque o valor para converter em Atbash: ")

# Usamos o recurso maketrans da biblioteca string 
transform = string.maketrans(
"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", # Alfabeto crescente
"ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba") # Alfabeto decrescente

# Depois, fazemos a transformação correta
final = string.translate(input, transform)

print final
