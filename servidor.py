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

def checklogin(msg):
    print("LOGIN")
    # verifica se pode autenticar ...
    if msg.login == usuario[0] and msg.senha == senha[0]:
        global token
        token = '378rbf9sd'
        return API.acklogin(token)
    else:
        return API.acklogin('000000000')

def maketest(msg):
    print("REQPROVA")
    # consulta o id para saber qual a prova correspondente
    '''
    global idprova
    global questoes
    return API.ackreqprova(idprova, questoes)
    '''

def reqresp(msg):
    print("REQRESP")
    print('Recebido pelo servidor: ', msg)

def reqresultado():
    print("REQRESULTADO")

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
        print('Esperando conexão...')
        con, addr = s.accept()
        data = con.recv(1024)

        msg,des = API.mensagem(data)
        if des=='login': # se for mensagem de login
            data = checklogin(msg)
            con.send(data)

        elif des=='reqprova':
            print('REQ_PROVA')

            # questoes = pegando_questoes()     # questoes é uma lista
            # API.ackreqprova(id_prova, questoes)

            con.send(API.ackreqprova())
            
        elif des=='reqresp':
            reqresp(msg)
            
        elif des=='reqresultado':
            reqresultado()
            
        elif des=='logout':
            logout(msg)

        print("token: ", token)