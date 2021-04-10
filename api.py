#!/usr/bin/env python3

import sys
import provaonline_pb2

LOGIN_INCORRETO = 111
LOGIN_APROVADO = 222

class API():
    
    def mensagem(data):
        msg = provaonline_pb2.MENSAGEM()
        msg.ParseFromString(data)
        # print('Mensagem recebida:\n', msg)

        if msg.HasField('login'):
            l = provaonline_pb2.LOGIN()
            l.login = msg.login.login
            l.senha = msg.login.senha    
            return l,"login"

        elif msg.HasField('acklogin'):
            a = provaonline_pb2.ACK_LOGIN()
            a.token = msg.acklogin.token
            a.status.codigo = msg.acklogin.status.codigo
            a.status.descricao = msg.acklogin.status.descricao
            return a,"acklogin"
            
        elif msg.HasField('reqprova'):
            # r = provaonline_pb2.REQ_PROVA()
            # r.token = msg.reqprova.token
            # r.id_prova = msg.reqprova.id_prova
            return msg,"reqprova"

        elif msg.HasField('ackreqprova'):
            # a = provaonline_pb2.ACK_REQ_PROVA()
            # a.id_prova = msg.ackreqprova.id_prova
            # a.questoes = msg.ackreqprova.questoes
            return msg,"ackreqprova"

        elif msg.HasField('reqresp'):
            # r = provaonline_pb2.REQ_RESP()
            # r.token = msg.reqresp.token
            # r.id_prova = msg.reqresp.id_prova
            # r.respostas = msg.reqresp.respostas
            return msg,"reqresp"

        elif msg.HasField('reqresultado'):
            r = provaonline_pb2.REQ_RESULTADO()
            r.token = msg.reqresultado.token
            r.id_prova = msg.reqresultado.id_prova
            return r,"reqresultado"

        elif msg.HasField('ackreqresultado'):
            a = provaonline_pb2.ACK_REQ_RESULTADO()
            a.id_prova = msg.ackreqresultado.id_prova
            a.nota = msg.ackreqresultado.nota
            a.questoes = msg.ackreqresultado.questoes
            return a,"ackreqresultado"
        
        elif msg.HasField('logout'):
            l = provaonline_pb2.LOGOUT()
            l.token = msg.logout.token
            return l,"logout"

    def login(usuario, senha):
        m = provaonline_pb2.MENSAGEM()
        m.login.login = usuario #string
        m.login.senha = senha #string
        return m.SerializeToString()
    
    def acklogin(token):
        m = provaonline_pb2.MENSAGEM()
        m.acklogin.token = token #string
        m.acklogin.status.codigo = LOGIN_APROVADO #int32
        m.acklogin.status.descricao = 'LOGIN APROVADO' #string
        return m.SerializeToString()

    def reqprova(token, id_prova):
        m = provaonline_pb2.MENSAGEM()
        m.reqprova.token = token #string
        m.reqprova.id_prova = id_prova #string
        return m.SerializeToString()
    
    def ackreqprova():
        m = provaonline_pb2.MENSAGEM()
        try:
            f = open('questoes.txt', "rb")
            m.ackreqprova.ParseFromString(f.read())
            f.close()
        except IOError:
            print("Could not open file.  Creating a new one.")
        return m.SerializeToString()
    
    def reqresp(token, id_prova, respostas, questoes):
        resp = list()
        for r in respostas:
            for q in questoes:
                if q.id == r[0]:
                    if len(q.alternativas) > 1: resp.append(API.resposta_optativa(r[0], r[1])) # crio obj resposta com api
                    else: resp.append(API.resposta_discursiva(r[0], r[1])) # crio obj resposta com api
                    break

        m = provaonline_pb2.MENSAGEM()
        m.reqresp.token = token #string
        m.reqresp.id_prova = id_prova #string
        for r in resp:
            rp = m.reqresp.respostas.add()
            rp.id = r.id
            if r.HasField('codigos'): 
                for c in r.codigos.codigos: rp.codigos.codigos.append(c)
            else: rp.texto = r.texto
            
        return m.SerializeToString()

    def reqresultado(token, id_prova):
        m = provaonline_pb2.MENSAGEM()
        m.reqresultado.token = token #string
        m.reqresultado.id_prova = id_prova #string
        return m.SerializeToString()
    
    def ackreqresultado(id_prova, nota, questoes):
        m = provaonline_pb2.MENSAGEM()
        m.ackreqresultado.id_prova = id_prova #string
        m.ackreqresultado.nota = nota #int32
        m.ackreqresultado.questoes = questoes #RESULTADO
        return m.SerializeToString()
    
    def logout(token):
        m = provaonline_pb2.MENSAGEM()
        m.logout.token = token #string
        return m.SerializeToString()

    # def questao(id, enunciado, pontos, alternativas):
    #     pass
    
    # def alternativa(descricao, codigo):
    #     pass

    def resposta_discursiva(id, texto):
        r = provaonline_pb2.RESPOSTA()
        r.id = id
        r.texto = texto
        return r
        
    def resposta_optativa(id, codigos):
        r = provaonline_pb2.RESPOSTA()
        r.id = id
        if type(codigos) is not list:
            r.codigos.codigos.append(codigos)
        else:
            for c in codigos: r.codigos.codigos.append(c)
        return r