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
        respostas = self.coletando_respostas() # respostas do aluno
        data = API.reqresp(self.token, self.prova.id_prova, respostas, self.prova.questoes) # parm questoes p/ verificar tipo resp
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
        respostas = list()
        respostas.append([654,['222','xxx']])
        respostas.append([987,'111'])
        respostas.append([321,"A Rosa dos Ventos eh um instrumento antigo utilizado para auxiliar na localizacao relativa."])
        return respostas