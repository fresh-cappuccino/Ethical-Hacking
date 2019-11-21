#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo faz a 
  implementação de 
  hashes em um cenário real
  com Bcrypt

  Modificado em 24 de janeiro de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

import sys

# Tentativa de importação das bibliotecas necessárias
try:
    import bcrypt
except:
    sys.exit("[!] Por favor, intale a biblioteca bcrypt com o comando: sudo pip install bcrypt")

# Digite uma senha
new = raw_input('Por favor insira uma senha: ')
# Vamos criptografar a senha com o bcrypt com o valor padrão 
hashed = bcrypt.hashpw(new, bcrypt.gensalt())
# Vamos imprimir o hash que acabamos de gerar
print('A string armazenada é: ' + hashed)
# Confirmar que introduzimos a senha correta
plaintext = raw_input('Digite novamente a senha para verificar: ')
# Verifique se ambas as senhas são as mesmas
if bcrypt.hashpw(plaintext, hashed) == hashed:
    print 'Senhas ok!'
else:
    print 'Erro de senhas! Por favor repita a operação.'






