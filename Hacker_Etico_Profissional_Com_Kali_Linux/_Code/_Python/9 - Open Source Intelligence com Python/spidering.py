#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo faz 
  capturação de páginas
  de um site.

  Modificado em 24 de dezembro de 2016
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Importantando as bibliotecas necessárias
import urllib2 
from bs4 import BeautifulSoup
import sys 


urls = []  # Um argumento de uma URL a ser colocado
urls2 = [] 

tarurl = sys.argv[1]

url = urllib2.urlopen(tarurl).read()
soup = BeautifulSoup(url)
for line in soup.find_all('a'):
    newline = line.get('href')
    print line.get('href')
    try:
	    if newline[:4] == "http":
	        if tarurl in newline:
	            urls.append(str(newline))
	        elif newline[:1] == "/":
	            combline = tarurl+newline
	            urls.append(str(combline))
    except:
        pass
for uurl in urls: 
    url = urllib2.urlopen(uurl).read()
    soup = BeautifulSoup(url)
    for line in soup.find_all('a'):
        newline = line.get('href')
        try:
		    if newline[:4] == "http":
		        if tarurl in newline:
		            urls2.append(str(newline))
		        elif newline[:1] == "/":
		            combline = tarurl+newline
		            urls2.append(str(combline))
        except:
            pass
urls3 = set(urls2)
for value in urls3:
    print value
