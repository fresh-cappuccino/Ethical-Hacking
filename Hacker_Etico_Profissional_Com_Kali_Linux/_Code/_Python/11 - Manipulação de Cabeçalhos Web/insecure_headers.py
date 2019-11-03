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
urls = open("urls.txt", "r") # O arquivo urls.txt deve existir!


# Interação de as possiveis vulnerabilidades que possam ser encontradas num servidor web
for url in urls:
	url = url.strip()
	req = requests.get(url)
	print url, 'report:'
	try:
		xssprotect = req.headers['X-XSS-Protection']
		if xssprotect != '1; mode=block':
			print 'X-XSS-Protection não está configurado corretamente, um ataque de XSS pode ser possível:', xssprotect
	except:
		print 'X-XSS-Protection não está configurado corretamente, um ataque de XSS pode ser possível'

	try:
		contenttype = req.headers['X-Content-Type-Options']
		if contenttype != 'nosniff':
			print 'X-Content-Type-Options não está configurado corretamente:', contenttype
	except:
		print 'X-Content-Type-Options não configurado'

	try:
			hsts = req.headers['Strict-Transport-Security']
	except:
		print 'O HSTS header não está configurado, ataques de MITM podem ser possiveis'

	try:
		csp = req.headers['Content-Security-Policy']
		print 'Content-Security-Policy configurado:', csp
	except:
		print 'Content-Security-Policy não está configurado corretamente'
		print '----'

	




