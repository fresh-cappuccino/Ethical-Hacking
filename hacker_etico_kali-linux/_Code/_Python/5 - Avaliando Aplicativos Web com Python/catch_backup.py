#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo faz a tentativa
  de fazer downloads de arquivos
  de backups.

  Modificado em 15 de dezembro de 2016
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""
# Importa as bibliotecas necessárias
import sys

try:
 import tftpy
except:
 sys.exit("[!] Instale a biblioteca tftpy com: pip install tftpy")


def main():
	ip = "192.168.1.1"  # Coloque o IP de seu alvo
	port = 22           # Coloque a porta alvo
	tclient = tftpy.TftpClient(ip,port)
	for inc in range(0,100):
		filename = "arquivo_criado" + "-" + str(inc)  # Nome do arquivo a ser salvo
		print("[*] Tentativa de download %s de %s:%s") % (filename,ip,port)
		try:
			tclient.download(filename,filename)
		except KeyboardInterrupt:  # Para interromper o programa aperte Crtl+C
			print 'Programa Interrompido'
			sys.exit()
		except:
			print("[-] Falha ao fazer o download %s de %s:%s") % (filename,ip,port)

if __name__ == '__main__':
	main()





