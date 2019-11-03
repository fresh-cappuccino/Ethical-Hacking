#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo faz a descoberta de 
  cifras de substituição para ASCII 

  Modificado em 26 de janeiro de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Colocamos a string aqui!
string ="TaPoGeTaBiGePoHfTmGeYbAtPtHoPoTaAuPtGeAuYbGeBiHoTaTmPtHoTmGePoAuGeErTaBiHoAuRnTmPbGePoHfTmGeTmRaTaBiPoTmPtHoTmGeAuYbGeTbGeLuTmPtTmPbTbOsGePbTmTaLuPtGeAuYbGeAuPbErTmPbGeTaPtGePtTbPoAtPbTmGeTbPtErGePoAuGeYbTaPtErGePoHfTmGeHoTbAtBiTmBiGeLuAuRnTmPbPtTaPtLuGePoHfTaBiGeAuPbErTmPbPdGeTbPtErGePoHfTaBiGePbTmYbTmPbBiGeTaPtGeTmTlAtTbOsGeIrTmTbBiAtPbTmGePoAuGePoHfTmGePbTmOsTbPoTaAuPtBiGeAuYbGeIrTbPtGeRhGeBiAuHoTaTbOsGeTbPtErGeHgAuOsTaPoTaHoTbOsGeRhGeTbPtErGePoAuGePoHfTmGeTmPtPoTaPbTmGeAtPtTaRnTmPbBiTmGeTbBiGeTbGeFrHfAuOsTmPd"

# fazendo as definições necessárias
n=2
list = [] # lista 
answer = [] # resposta 

# percorre a seqüência de caracteres e removeu os conjuntos de duas letras e coloca ao valor da lista
[list.append(string[i:i+n]) for i in range(0, len(string), n)]

# printa a lista que foi formatada 
print set(list)

# Dicionários dos valores da sting ao formato ASCII equivalente
periodic ={"Pb": 82, "Tl": 81, "Tb": 65, "Ta": 73, "Po": 84, "Ge":
32, "Bi": 83, "Hf": 72, "Tm": 69, "Yb": 70, "At": 85, "Pt": 78,
"Ho": 67, "Au": 79, "Er": 68, "Rn": 86, "Ra": 88, "Lu": 71,
"Os": 76, "Tl": 81, "Pd": 46, "Rh": 45, "Fr": 87, "Hg": 80,
"Ir": 77}

# Faz uma interação sobre toda a lista e fazendo a conversão em numeros em caracteres do nosso alfabeto
for value in list:
	if value in periodic:
		answer.append(chr(periodic[value]))

# Finalmente, precisamos ter os dados impressos para nós.
lastanswer = ''.join(answer)
print lastanswer





