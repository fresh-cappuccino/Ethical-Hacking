#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo tenta 
  fazer a tentativa de 
  negação de autenticação

  Modificado em 19 de dezembro de 2016
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Importação das bibliotecas necessárias
from scapy.all import *

interface = 'wlan1mon' # Interface de rede em modo monitor
i=1

# Função que faz a deteccção de ataques de desautenticação
def info(fm):
	if fm.haslayer(Dot11):
		if ((fm.type == 0) & (fm.subtype==12)):
			global i
			print "Tentativa de negação foi detatectado ", i
			i=i+1
						
sniff(iface=interface,prn=info)






