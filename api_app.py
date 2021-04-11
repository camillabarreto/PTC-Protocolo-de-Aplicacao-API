#!/usr/bin/env python3

import sys
import provaonline_pb2
from socket import*

ACK = 000 # ack ok
NACK = 999 # ack not ok

class API_APP():
    def __init__(self, ip, port):
        self.token = ''
        self.ip = ip
        self.port = port
        self.socket = None
    
    def send(self, data):
        self.socket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
        self.socket.bind(('0.0.0.0', 0))
        self.socket.connect((self.ip, self.port))
        self.socket.send(data) # envia dados pelo socket
        data = self.socket.recv(1024)
        self.socket.shutdown(SHUT_RDWR)  
        msg = provaonline_pb2.MENSAGEM()
        msg.ParseFromString(data)
        return msg
    
    def login(self, usuario, senha):
        ms = provaonline_pb2.MENSAGEM()
        ms.login.login = usuario #string
        ms.login.senha = senha #string
        mr = self.send(ms.SerializeToString())
        if mr.acklogin.status.codigo == NACK:
            return False  #, mr.acklogin.status.descricao
        else:
            self.token = mr.acklogin.token
            return True
    
    def reqprova(self, id_prova):
        ms = provaonline_pb2.MENSAGEM()
        ms.reqprova.token = self.token #string
        ms.reqprova.id_prova = id_prova #string
        mr = self.send(ms.SerializeToString())
        if mr.HasField('status'):
            return False, mr.acklogin.status.descricao
        else:
            return True, mr.ackreqprova.questoes

    def reqresp(self, id_prova, respostas): # respostas é uma lista
        ms = provaonline_pb2.MENSAGEM()
        ms.reqresp.token = self.token #string
        ms.reqresp.id_prova = id_prova #string
        for r in respostas:
            rp = ms.reqresp.respostas.add()
            rp.id = r.id
            if r.HasField('codigos'): 
                for c in r.codigos.codigos: rp.codigos.codigos.append(c)
            else: rp.texto = r.texto
        mr = self.send(ms.SerializeToString())
        if mr.status.codigo == NACK:
            return False, mr.acklogin.status.descricao
        else:
            return True, None
        
    def reqresultado(self, id_prova):
        ms = provaonline_pb2.MENSAGEM()
        ms.reqresultado.token = self.token #string
        ms.reqresultado.id_prova = id_prova #string
        mr = self.send(ms.SerializeToString())
        if mr.HasField('status'):
            return False, mr.status.descricao
        else:
            return True, mr.ackreqresultado

    def logout(self):
        ms = provaonline_pb2.MENSAGEM()
        ms.logout.token = self.token #string
        mr = self.send(ms.SerializeToString())
        if mr.status.codigo == NACK:
            return False, mr.status.descricao
        else: 
            return True, None
