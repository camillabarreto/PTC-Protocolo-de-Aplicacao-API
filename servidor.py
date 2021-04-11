#!/usr/bin/env python3

import sys
from socket import*
import provaonline_pb2
from api import API

# LOGIN
usuario = ["aluno"]
senha = ["aluno"]
token = None

# PROVA
idprova = '11233'

ACK = 000 # ack ok
NACK = 999 # ack not ok

def checklogin(msg):
    print("LOGIN")
    # verifica se pode autenticar ...
    if msg.login == usuario[0] and msg.senha == senha[0]:
        global token
        token = '378rbf9sd'
        return API.acklogin(token)
    else:
        return API.acklogin('000000000')

# def reqresp(msg):
#     print("REQRESP")
#     print('Recebido pelo servidor: ', msg)

# def reqresultado():
#     print("REQRESULTADO")

def logout(msg):
    print("LOGOUT")
    global token
    token = None

# def pegando_questoes():

#     # arq q1 -> questao1
#     # arq q2-> questao2
#     # arq q3-> questao3
    
#     # return lista de questoes


if __name__ == '__main__':
    s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
    s.bind(('0.0.0.0', 8888))
    s.listen()  # espera conexões na porta

    while True:
        print('\nEsperando conexão...')
        con, addr = s.accept()
        data = con.recv(1024)

        msg = provaonline_pb2.MENSAGEM()
        msg.ParseFromString(data)
        if msg.HasField('login'):
            mr = provaonline_pb2.MENSAGEM()
            if msg.login.login == "aluno" and msg.login.senha == "aluno":
                mr.acklogin.token = '378rbf9sd'
                mr.acklogin.status.codigo = ACK
                print("ACK LOGIN")
            else: 
                mr.acklogin.status.codigo = NACK 
                print("NACK LOGIN")
            con.send(mr.SerializeToString())

        elif msg.HasField('reqprova'):
            print('REQ_PROVA')
            con.send(API.ackreqprova())
            
        elif msg.HasField('reqresp'):
            # reqresp(msg)
            print('Recebido pelo servidor: ', msg)
            
        elif msg.HasField('reqresultado'):
            # reqresultado()
            print('Recebido pelo servidor: ', msg)
            
        elif msg.HasField('logout'):
            logout(msg)