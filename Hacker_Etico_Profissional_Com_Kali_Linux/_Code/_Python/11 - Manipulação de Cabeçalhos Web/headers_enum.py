#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo tenta
  verificar as possiveis 
  vulnerabilidades de um site

  Modificado em 26 de dezembro de 2016
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Importantando as bibliotecas necessárias
import requests

req = requests.get('http://siteteste.com.br')
headers = ['Server', 'Date', 'Via', 'X-Powered-By']

for header in headers:
    try:
	result = req.headers[header]
        print '%s: %s' % (header, result)
    except Exception, error:
        pass













