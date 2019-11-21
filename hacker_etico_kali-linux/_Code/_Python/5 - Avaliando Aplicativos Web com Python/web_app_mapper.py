#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo faz escaneamento 
  de diretórios e arquvios dentro
  de websites

  Modificado em 14 de dezembro de 2016
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Importa as bibliotecas necessárias
import Queue
import threading
import os
import urllib2

threads   = 10  # Número de threads

target    = "http://www.exemplodesite.com"      # Domínio do site
directory = "/"  # Diretório a ser escaneado
filters   = [".jpg",".gif","png",".css"]  # Tipos de Arquivos Filtrados

os.chdir(directory)

web_paths = Queue.Queue() 


# Função que percorre todos os arquivos e diretórios no diretório local da aplicação web.
for r,d,f in os.walk("."): 
    for files in f:
        remote_path = "%s/%s" % (r,files)
        if remote_path.startswith("."):
            remote_path = remote_path[1:]
        if os.path.splitext(files)[1] not in filters:
            web_paths.put(remote_path)

def test_remote():
    while not web_paths.empty(): 
        path = web_paths.get()
        url = "%s%s" % (target, path)

        request = urllib2.Request(url) 

        try:
            response = urllib2.urlopen(request)
            content  = response.read()

            print "[%d] => %s" % (response.code,path) 

            response.close()
        
        except urllib2.HTTPError as error: 
            # imprime erro de execução "Failed %s" % error.code
            pass
        
        

for i in range(threads): 
    print "Espalhando thread: %d" % i
    t = threading.Thread(target=test_remote)
    t.start()
