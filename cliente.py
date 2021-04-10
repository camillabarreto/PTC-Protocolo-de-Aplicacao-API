#!/usr/bin/env python3

import sys
from socket import*
import provaonline_pb2
from api import API

class Cliente():
    def __init__(self, login, senha):
        self.usuario = login
        self.senha = senha
        self.token = ''
        self.prova = None


    def connect(self, data):
        # Cria conexão por socket
        self.s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
        self.s.bind(('0.0.0.0', 0))
        self.s.connect(('127.0.0.1', 8888)) # passar IP de destino por argumento de linha
        self.s.send(data) # envia dados pelo socket
    
    def shutdown(self):
        self.s.shutdown(SHUT_RDWR)  
        
    def login(self):
        data = API.login(self.usuario, self.senha)
        print('Mensagem codificada:', data)
        self.connect(data) # envia dados pelo socket

        resp = self.s.recv(1024)
        msg,des = API.mensagem(resp)
        if des=='acklogin': # se for mensagem de acklogin
            print('Resposta servidor:\n', msg)
            print("token: ",msg.token)
            self.token = msg.token
        self.shutdown() 

    
    def logout(self):
        data = API.logout(self.token)
        print('Mensagem codificada:', data)
        self.connect(data) # envia dados pelo socket
        self.shutdown()

    def reqprova(self, id_prova):
        data = API.reqprova(self.token, id_prova)
        print('Mensagem codificada:', data)
        self.connect(data) # envia dados pelo socket
        
        ## espera ack
        resp = self.s.recv(1024)
        msg,des = API.mensagem(resp)
        if des=='ackreqprova': # se for mensagem de ackreqprova
            print('Resposta servidor:\n', msg)
            self.prova = msg.ackreqprova
        self.shutdown()

    def reqresp(self):
        # crio resposta com api
        respostas = [[654,['222','xxx']],[987,'111'],[321,"A Rosa dos Ventos eh um instrumento antigo utilizado para auxiliar na localizacao relativa."]]
        resp = []
        for r in respostas:
            print("resposta : ",r)
            for q in self.prova.questoes:
                print("questao : ",q)
                if q.id == r[0]:
                    if len(q.alternativas) > 1: 
                        print("optativa")
                        resp.append(API.resposta_optativa(r[0], r[1]))
                    else: 
                        print("discursiva")
                        resp.append(API.resposta_discursiva(r[0], r[1]))
                    break
        
        # respostas = self.coletando_respostas()
        data = API.reqresp(self.token, self.prova.id_prova, resp)
        print('Mensagem codificada:', data)
        self.connect(data) # envia dados pelo socket
        self.shutdown()
    
    def reqresultado(self, token, id_prova):
        data = API.reqresultado(self.token, id_prova)
        print('Mensagem codificada:', data)
        self.connect(data) # envia dados pelo socket
        
        ## espera ack
        resp = self.s.recv(1024)
        msg,des = API.mensagem(resp)
        if des=='ackreqresultado': # se for mensagem de acklogin
            print('Resposta servidor:\n', msg)
        self.shutdown()
    
    def logout(self):
        data = API.logout(self.token)
        print('Mensagem codificada:', data)
        self.connect(data) # envia dados pelo socket

        ## ack??
        self.shutdown()

    
    def coletando_respostas(self): # Respostas estáticas
        
        # R1
        resp1 = provaonline_pb2.RESPOSTA()
        resp1.id = 654
        resp1.codigos.codigos.append('222')
        
        # R2
        resp2 = provaonline_pb2.RESPOSTA()
        resp2.id = 987
        resp2.codigos.codigos.append('111')
        
        # R3
        resp3 = provaonline_pb2.RESPOSTA()
        resp3.id = 321
        resp3.texto = "A Rosa dos Ventos eh um instrumento antigo utilizado para auxiliar na localizacao relativa."

        return [resp1, resp2, resp3]