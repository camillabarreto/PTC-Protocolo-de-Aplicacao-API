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

def pegando_questoes():
    questao1 = provaonline_pb2.QUESTAO()
    questao1.id = 654
    questao1.enunciado = 'Qual a capital de Santa Catarina?'
    questao1.pontos = 5
    alternativa11 = questao1.alternativas.add()
    alternativa11.codigo = '111'
    alternativa11.descricao = '(a) Sao Paulo'
    alternativa12 = questao1.alternativas.add()
    alternativa12.codigo = '222'
    alternativa12.descricao = '(b) Florianopolis'
    alternativa13 = questao1.alternativas.add()
    alternativa13.codigo = '333'
    alternativa13.descricao = '(c) Sao Paulo'
    questao2 = provaonline_pb2.QUESTAO()
    questao2.id = 987
    questao2.enunciado = 'Qual a capital de Pernambuco?'
    questao2.pontos = 5
    alternativa21 = questao2.alternativas.add()
    alternativa21.codigo = '111'
    alternativa21.descricao = '(a) Recife'
    alternativa22 = questao2.alternativas.add()
    alternativa22.codigo = '222'
    alternativa22.descricao = '(b) Aracaju'
    alternativa23 = questao2.alternativas.add()
    alternativa23.codigo = '333'
    alternativa23.descricao = '(c) Goiania'
    questao3 = provaonline_pb2.QUESTAO()
    questao3.id = 321
    questao3.enunciado = 'Qual a utilidade da Rosa dos Ventos?'
    questao3.pontos = 4
    return [questao1, questao2, questao3]

if __name__ == '__main__':
    s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
    s.bind(('0.0.0.0', 8888))
    s.listen()  # espera conexões na porta
    token = '378rbf9sd'
    id_prova = '1'
    questoes = pegando_questoes()

    while True:
        print('\nEsperando conexão...')
        con, addr = s.accept()
        data = con.recv(1024)

        msg = provaonline_pb2.MENSAGEM()
        msg.ParseFromString(data)
        mr = provaonline_pb2.MENSAGEM()
        if msg.HasField('login'):
            if msg.login.login == "aluno" and msg.login.senha == "aluno":
                mr.acklogin.token = token
                mr.acklogin.status.codigo = ACK
                print("ACK LOGIN")
            else: 
                mr.acklogin.status.codigo = NACK 
                print("NACK LOGIN")

        elif msg.HasField('reqprova'):
            if msg.reqprova.id_prova == id_prova and msg.reqprova.token == token:
                mr.ackreqprova.id_prova = id_prova
                for q in questoes:
                    y = mr.ackreqprova.questoes.add()
                    y.id = q.id
                    y.enunciado = q.enunciado
                    y.pontos = q.pontos
                    if len(q.alternativas) > 1: # caso seja optativa
                        for a in q.alternativas:
                            z = y.alternativas.add()
                            z.descricao = a.descricao
                            z.codigo = a.codigo
                print('ACK REQ_PROVA')
            else:
                mr.acklogin.status.codigo = NACK 
                print("NACK REQ PROVA")
            
        elif msg.HasField('reqresp'):
            # if msg.reqprova.id_prova == id_prova and msg.reqprova.token == token:
            #     mr.ackreqprova.id_prova = id_prova
            #     mr.ackreqprova.questoes = questoes
            #     print('ACK REQ_PROVA')
            # else:
            #     mr.acklogin.status.codigo = NACK 
            #     print("NACK LOGIN")
            pass
            
        elif msg.HasField('reqresultado'):
            # reqresultado()
            print('Recebido pelo servidor: ', msg)
            
        elif msg.HasField('logout'):
            logout(msg)
        
        con.send(mr.SerializeToString())