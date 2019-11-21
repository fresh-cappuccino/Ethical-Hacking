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

# Testando todos os métodos existentes
verbs = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'TRACE','TEST']

for verb in verbs:
	req = requests.request(verb, 'http://testeseusite.com.br') # Coloque o seu site alvo aqui!
	print verb, req.status_code, req.reason
	if verb == 'TRACE' and 'TRACE / HTTP/1.1' in req.text:
		print 'Possível vulnerabilidade de Cross Site Tracing encontrada' 









