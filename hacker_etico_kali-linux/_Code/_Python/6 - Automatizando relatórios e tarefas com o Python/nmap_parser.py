#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo faz o testes de portas
  abertas, mais especificamente na porta
  80

  Modificado em 16 de dezembro de 2016
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Importação das bibliotecas necessárias
import sys
import xml.etree.ElementTree as etree
import argparse
import collections

try:
    import nmap_doc_generator as gen
except Exception as e:
    print(e)
    sys.exit("[!] Por favor coloque o arquivo nmap_doc_generator.py nesse mesmo diretório")

class Nmap_parser:
    def __init__(self, nmap_xml, verbose=0):
        self.nmap_xml = nmap_xml
        self.verbose = verbose
        self.hosts = {}
        try:
            self.run()
        except Exception, e:
            print("[!] Havia um erro %s") % (str(e))
            sys.exit(1)

    def run(self):
        # Analise o arquivo nmap xml e extraia os hosts e coloque-os em um dicionário
        # Input: Arquivo XML Nmap e sinalizador detalhado
        # Retorno: Dicionário de hosts [número iterado] = [nome do host, endereço, protocolo, porta, nome do serviço, estado]
        if not self.nmap_xml:
            sys.exit("[!] Não é possível abrir o arquivo Nmap XML: %s \n[-] Certifique-se de que você está passando o arquivo correto e o seu formato" % (self.nmap_xml))
        try:
            tree = etree.parse(self.nmap_xml)
        except:
            sys.exit("[!] Não é possível abrir o arquivo Nmap XML: %s \n[-] Certifique-se de que você está passando o arquivo correto e o seu formato" % (self.nmap_xml))
        hosts={}
        services=[]
        hostname_list=[]
        root = tree.getroot()
        hostname_node = None
        if self.verbose > 0:
            print ("[*] Analisando o arquivo XML Nmap: %s") % (self.nmap_xml)
        for host in root.iter('host'):
            hostname = "Unknown hostname"
            for addresses in host.iter('address'):
                hwaddress = "No MAC Address ID'd"
                ipv4 = "No IPv4 Address ID'd"
                addressv6 = "No IPv6 Address ID'd"
                temp = addresses.get('addrtype')
                if "mac" in temp:
                    hwaddress = addresses.get('addr')
                    if self.verbose > 2:
                        print("[*] O host estava no mesmo domínio de broadcast")
                if "ipv4" in temp:
                    address = addresses.get('addr')
                    if self.verbose > 2:
                        print("[*] O host tinha um endereço IPv4")
                if "ipv6" in temp:
                    addressv6 = addresses.get('addr')
                    if self.verbose > 2:
                        print("[*] O host tinha um endereço IPv6")
            try:
                hostname_node = host.find('hostnames').find('hostname')
            except:
                if self.verbose > 1:
                    print ("[!] Nenhum hostname encontrado")
            if hostname_node is not None:
                hostname = hostname_node.get('name')
            else:
                hostname = "Unknown hostname"
                if self.verbose > 1:
                    print("[*] O nome do host é %s") % (str(hostname_node))
            hostname_list.append(hostname)
            for item in host.iter('port'):
                state = item.find('state').get('state')
                # if state.lower() == 'open':
                service = item.find('service').get('name')
                protocol = item.get('protocol')
                port = item.get('portid')
                services.append([hostname_list, address, protocol, port, service, hwaddress, state])
        hostname_list=[]
        for i in range(0, len(services)):
            service = services[i]
            index = len(service) - 1
            hostname = str1 = ''.join(service[0])
            address = service[1]
            protocol = service[2]
            port = service[3]
            serv_name = service[4]
            hwaddress = service[5]
            state = service[6]
            self.hosts[i] = [hostname, address, protocol, port, serv_name, hwaddress, state]
            if self.verbose > 2:
                print ("[+] Adicionando %s com um IP de %s:%s com o serviço %s")%(hostname,address,port,serv_name)
        if self.hosts:
            if self.verbose > 4:
                print ("[*] Resultados da importação XML do NMAP: ")
                for key, entry in self.hosts.iteritems():
                    print("[*] %s") % (str(entry))
            if self.verbose > 0:
                print ("[+] Portas únicas analisadas e importadas %s") % (str(i+1))
        else:
            if self.verbose > 0:
                print ("[-] Nenhuma porta foi descoberta no arquivo XML NMAP")

    def hosts_return(self):
        # A controlled return method
        # Input: None
        # Returned: The processed hosts
        try:
             return self.hosts
        except Exception as e:
            print("[!] Ocorreu um erro ao retornar os dados %s") % (e)

if __name__ == '__main__':
    # If script is executed at the CLI
    usage = '''Modo de usar: %(prog)s [-x reports.xml] [-f xml_output2.xlsx] -s -q -v -vv -vvv'''
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument("-x", "--xml", type=str, help="Gerar um dicionário de dados com base em uma importação NMAP XML, mais de um arquivo pode ser passado, separados por uma vírgula", action="store", dest="xml")
    parser.add_argument("-f", "--filename", type=str, action="store", dest="filename", default="xml_output", help="O nome de arquivo que será usado para criar um XLSX")
    parser.add_argument("-s", "--simple", action="store_true", dest="simple", help="Formate a saída em um produto simples do excel, em vez de um relatório")
    parser.add_argument("-v", action="count", dest="verbose", default=1, help="Nível de verbosidade, padrão para um, este produz cada comando e resultado")
    parser.add_argument("-q", action="store_const", dest="verbose", const=0, help="Define os resultados como silenciosos")
    parser.add_argument('--version', action='version', version='%(prog)s 0.43b')
    args = parser.parse_args()

    # Argumento validador
    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    
    xml = args.xml                      # nmap XML
    if not xml:
        sys.exit("[!] No XML file provided")
    verbose = args.verbose              # Nível de Verbosidade
    filename = args.filename            # Nome do arquivo para saída XLSX
    simple = args.simple          # Define as cores da saída da planilha do Excel
    xml_list=[]                         # Lista para armazenar as XMLs

    # Definir titular de retorno
    hosts=[]                            # Lista para armazenar instâncias
    hosts_temp={}                       # Dicionário temporário, que contém dados retornados de instâncias específicas
    hosts_dict={}                       # Dicionário, que detém os dicionários devolvidos combinados
    processed_hosts={}                  # O dicionário, que contém os valores exclusivos de todos os XMLs processados
    count = 0                           # Contagem para combinar dicionários
    unique = set()


    # Instanciação para comprovação de conceito
    if "," in xml:
        xml_list = xml.split(',')
    else:
        xml_list.append(xml)
    for x in xml_list:
        try:
            tree_temp = etree.parse(x)
        except:
            sys.exit("[!] Não é possível abrir o arquivo XML: %s \n[-] Certifique-se de que você está passando o arquivo correto e formato" % (x))
        try:
            root = tree_temp.getroot()
            name = root.get("scanner")
            if name is not None and "nmap" in name:
                if verbose > 1:
                    print ("[*] Arquivo sendo processado é um NMAP XML")
                hosts.append(Nmap_parser(x, verbose))
            else:
                print("[!] O arquivo % não é um NMAP XML") % (str(x))
                sys.exit(1)
        except Exception, e:
            print("[!] Processamento de arquivo %s falhou %s") % (str(x), str(e))
            sys.exit(1)

    # Processamento de cada instância retornado para criar um dicionário composto
    if not hosts:
        sys.exit("[!] Ocorreu um problema ao processar os dados")
    for inst in hosts:
        hosts_temp = inst.hosts_return()
        if hosts_temp is not None:
            for k, v in hosts_temp.iteritems():
                hosts_dict[count] = v
                count+=1
            hosts_temp.clear()
    if verbose > 3:
        for key, value in hosts_dict.iteritems():
            print("[*] Chave: %s Valor: %s") % (key,value)
    temp = [(k, hosts_dict[k]) for k in hosts_dict]
    temp.sort()
    key = 0
    for k, v in temp:
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        if str(v) in str(processed_hosts.values()):
            continue
        else:
            key+=1
            processed_hosts[key] = v

    # Gerador para documentos XLSX
    gen.Nmap_doc_generator(verbose, processed_hosts, filename, simple)
