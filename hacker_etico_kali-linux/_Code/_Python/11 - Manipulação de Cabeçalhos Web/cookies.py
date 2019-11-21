#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo tenta
  verificar as seguranças 
  dos cookies dos sites

  Modificado em 29 de dezembro de 2016
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Importantando as bibliotecas necessárias
import requests
import time

# Função que verifica o HTTP
def check_httponly(c):
	if 'httponly' in c._rest.keys():
		return True
	else:
		return '\x1b[31mFalse\x1b[39;49m'

values = []
for i in xrange(0,5):
	req = requests.get('http://www.facebook.com') # Site alvo 
	for cookie in req.cookies:
		print 'Name:', cookie.name
		print 'Value:', cookie.value
		values.append(cookie.value)
		if not cookie.secure:
			cookie.secure = '\x1b[31mFalse\x1b[39;49m'
		print 'HTTPOnly:', check_httponly(cookie), '\n'
	time.sleep(2)

print set(values)










