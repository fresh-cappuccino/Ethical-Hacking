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
import sys
import time

try:
	from PyQt4.QtCore import *
	from PyQt4.QtGui import *
	from PyQt4.QtWebKit import *
except:
    sys.exit("[!] Por favor, intale as bibliotecas do PyQt4 com o comando: sudo apt-get install python2.7-dev libxext-dev python-qt4 qt4-dev-tools build-essential")

# Classe que define toda a programação
class Screenshot(QWebView):
    def __init__(self):
        self.app = QApplication(sys.argv)
        QWebView.__init__(self)
        self._loaded = False
        self.loadFinished.connect(self._loadFinished)

	# Função que faz o carregamendo da imagem
    def wait_load(self, delay=0):
        while not self._loaded:
            self.app.processEvents()
            time.sleep(delay)
        self._loaded = False

	# Função que termina de fazer a captura de tela
    def _loadFinished(self, result):
        self._loaded = True

	# Função que pega a imagem do site alvo
    def get_image(self, url):
        self.load(QUrl(url))
        self.wait_load()
       
        frame = self.page().mainFrame()
        self.page().setViewportSize(frame.contentsSize())
      
        image = QImage(self.page().viewportSize(), QImage.Format_ARGB32)
        painter = QPainter(image)
        frame.render(painter)
        painter.end()
        return image

s = Screenshot()
image = s.get_image('http://www.vmzsolutions.com.br') # Coloque o seu site alvo aqui!
image.save('website.png')











