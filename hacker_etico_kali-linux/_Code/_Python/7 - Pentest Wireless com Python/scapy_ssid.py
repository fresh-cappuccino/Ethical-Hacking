#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo printa os 
  rotadores wifi presentes 
  na area com o uso do Dot11

  Modificado em 19 de dezembro de 2016
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Importação das bibliotecas necessárias
from scapy.all import *
import struct

interface = 'wlan1mon' # Qual é o adaptador Wifi você deseja usar
ap_list = [] # Uma lista vazia de pontos de acessos sem fio

# Função que pega as informações com o uso do 'Dot11' 
def info(fm):
	if fm.haslayer(Dot11):
		if ((fm.type == 0) & (fm.subtype==8)):
			if fm.addr2 not in ap_list:
				ap_list.append(fm.addr2)
				print "SSID--> ",fm.info,"-- BSSID --> ",fm.addr2, \
"-- Canal--> ", ord(fm[Dot11Elt:3].info)	# Vai imprimir os SSID, os seus BSSID e seus canais de frequência
				
sniff(iface=interface,prn=info)











