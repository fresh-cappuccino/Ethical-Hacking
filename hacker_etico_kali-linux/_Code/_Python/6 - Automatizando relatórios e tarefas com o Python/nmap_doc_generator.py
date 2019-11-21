#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo faz a criação de
  uma planilha em EXCEL com informações
  recebidos pelo arquivo nmap_parser.py

  Modificado em 16 de dezembro de 2016
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Importação das bibliotecas necessárias
import sys
try:
    import xlsxwriter
except:
    sys.exit("[!] Instale a biblioteca xlsx writer com o comando: pip install xlsxwriter")


class Nmap_doc_generator():
    def __init__(self, verbose, hosts_dict, filename, simple):
        self.hosts_dict = hosts_dict
        self.filename = filename
        self.verbose = verbose
        self.simple = simple
        try:
            self.run()
        except Exception as e:
            print(e)

    def run(self):
        print ("") # DEBUG
        # Execute o módulo apropriado
        if self.verbose > 0:
            print ("[*] Construindo o arquivo %s.xlsx") % (self.filename)
            self.generate_xlsx()

    def generate_xlsx(self):
        if "xls" or "xlsx" not in self.filename:
            self.filename = self.filename + ".xlsx"
        workbook = xlsxwriter.Workbook(self.filename)
        # Formatando uma linha
        format1 = workbook.add_format({'bold': True})
		# Cor do cabeçalho
		# Pode ser encontrado em: http://www.w3schools.com/tags/ref_colorpicker.asp
	if self.simple:
            format1.set_bg_color('#538DD5')
	else:
	    format1.set_bg_color('#33CC33') # Formato do relatório
        # Formatação de linha para deixar uniforme
        format2 = workbook.add_format({'text_wrap': True})
        format2.set_align('left')
        format2.set_align('top')
        format2.set_border(1)
        # Formatação de linha ímpar
        format3 = workbook.add_format({'text_wrap': True})
        format3.set_align('left')
        format3.set_align('top')
		# Cor da linha
	if self.simple:
	    format3.set_bg_color('#C5D9F1') 
	else:
	    format3.set_bg_color('#99FF33') # Formato do relatório 
        format3.set_border(1)
        if self.verbose > 0:
            print ("[*] Criando uma pasta de trabalho: %s") % (self.filename)
        # Generate Worksheet 1
        worksheet = workbook.add_worksheet("Todas as portas")
        # Column width for worksheet 1
        worksheet.set_column(0, 0, 20)
        worksheet.set_column(1, 1, 17)
        worksheet.set_column(2, 2, 22)
        worksheet.set_column(3, 3, 8)
        worksheet.set_column(4, 4, 26)
        worksheet.set_column(5, 5, 13)
        worksheet.set_column(6, 6, 12)
        # Definir o local inicial para a Planilha 1
        row = 1
        col = 0
        # Gerar a linha 1 para a planilha 1
        worksheet.write('A1', "hostname", format1)
        worksheet.write('B1', "address", format1)
        worksheet.write('C1', "hwaddress", format1)
        worksheet.write('D1', "port", format1)
        worksheet.write('E1', "service_name", format1)
        worksheet.write('F1', "protocol", format1)
        worksheet.write('G1', "state", format1)
        worksheet.autofilter('A1:G1')
        # Preencher a planilha 1
        for key, value in self.hosts_dict.items():
            try:
                hostname = value[0]
                address = value[1]
                protocol = value[2]
                port = value[3]
                service_name = value[4]
                hwaddress = value[5]
                state = value[6]
            except:
                if self.verbose > 3:
                    print("[!] Ocorreu um erro ao analisar o ID do host: %s para a planilha 1") % (key)
            try:
                if row % 2 != 0:
                    temp_format = format2
                else:
                    temp_format = format3
                worksheet.write(row, col,     hostname, temp_format)
                worksheet.write(row, col + 1, address, temp_format)
                worksheet.write(row, col + 2, hwaddress, temp_format)
                worksheet.write(row, col + 3, port, temp_format)
                worksheet.write(row, col + 4, service_name, temp_format)
                worksheet.write(row, col + 5, protocol, temp_format)
                worksheet.write(row, col + 6, state, temp_format)
                row += 1
            except:
                if self.verbose > 3:
                    print("[!] Ocorreu um erro ao escrever os dados para a planilha 1")
        try:
            workbook.close()
        except:
            sys.exit("[!] Permissão para escrever no arquivo ou local fornecido foi negado")
