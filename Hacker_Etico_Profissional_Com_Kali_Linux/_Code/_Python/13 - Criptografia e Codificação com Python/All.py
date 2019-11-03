#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo faz comparações de 
  hashes SHA e MD5

  Modificado em 24 de janeiro de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Importação das bibliotecas necessárias
import hashlib

message = raw_input("Escreva uma string para hash: ")

md5 = hashlib.md5(message)
md5 = md5.hexdigest()

sha1 = hashlib.sha1(message)
sha1 = sha1.hexdigest()

sha256 = hashlib.sha256(message)
sha256 = sha256.hexdigest()

sha512 = hashlib.sha512(message)
sha512 = sha512.hexdigest()

print "Hash MD5 =", md5
print "Hash SHA1 =", sha1
print "Hash SHA256 =", sha256
print "Hash SHA512=", sha512
print "Fim da lista."








