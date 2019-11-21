#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo faz a 
  implementação de 
  hashes em um cenário real

  Modificado em 24 de janeiro de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Importação das bibliotecas necessárias
import uuid
import hashlib
 
def hash(password):
    salt = uuid.uuid4().hex
    return hashlib.sha512(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
def check(hashed, p2):
    password, salt = hashed.split(':')
    return password == hashlib.sha512(salt.encode() + p2.encode()).hexdigest()
 
password = raw_input('Por favor insira uma senha: ')

hashed = hash(password)

print('A seqüência de caracteres a ser armazenada no db é: ' + hashed)

re = raw_input('Por favor, digite sua senha novamente: ')

if check(hashed, re):
    print('OK! Senhas digitadas iguais')
else:
    print('ERROR! Senhas digitadas diferentes')






