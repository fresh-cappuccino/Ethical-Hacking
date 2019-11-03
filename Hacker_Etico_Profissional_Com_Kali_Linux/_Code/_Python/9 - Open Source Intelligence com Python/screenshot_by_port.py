#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo faz 
  capturação de imagens
  de sites usando o Python 

  Modificado em 23 de dezembro de 2016
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Importantando as bibliotecas necessárias
import screenshot # Importa o outro arquivo feito na outra aula, o screenshot.py.
import requests

# Lista de portas que vamos fazer uma examinação, pode acrescentar ou remover caso queira. Fique a vontade!
portList = [80,443,2082,2083,2086,2087,2095,2096,8080,8880, 8888,8008,8443,9998,4643,9001,4489]

IP = raw_input("Coloque a URL do alvo: ")

# Vamos pegar ambos os protocolos
http = 'http://'
https = 'https://'

# Função que faz o teste 200, e depois salva a imagem.
def testAndSave(protocol, portNumber):
    url = protocol + IP + ':' + str(portNumber)
    try:
        r = requests.get(url,timeout=1)
        
        if r.status_code == 200:
            print 'Site encontrado em ' + url 
            s = screenshot.Screenshot()
            image = s.get_image(url)
            image.save(str(portNumber) + '.png')
    except:
        pass

# Faz a interação das portas no seu site alvo.
for port in portList:
    testAndSave(http, port)
    testAndSave(https, port)







