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
    arquivos = ['questao1.txt', 'questao2.txt', 'questao3.txt']
    questoes = list()
    if msg.reqprova.id_prova == idprova:
        for arq in arquivos:
            try:
                f = open(arq, "rb")
                questoes.append(f.read())
                f.close()
            except IOError:
                print("Could not open file. Creating a new one.")
        return API.ackreqprova(idprova, questoes)
    # else:
    #     return API.ackreqprova('questoes.txt')

def reqresp():
    print("REQRESP")

def reqresultado():
    print("REQRESULTADO")

    # if msg.id_prova == idprova:
    #     return API.ackreqresultado(id_prova, 8, questoes)

def logout(msg):
    print("LOGOUT")
    global token
    token = None

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
            data = maketest(msg)
            con.send(data)
            
        elif des=='reqresp':
            reqresp()
            
        elif des=='reqresultado':
            data = reqresultado()
            con.send(data)
            
        elif des=='logout':
            logout(msg)

        print("token: ", token)