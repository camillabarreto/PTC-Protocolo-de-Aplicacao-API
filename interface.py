#!/usr/bin/env python3

from api_app import API_APP
import provaonline_pb2

LOGIN = '1'
PROVA = '2'
RESPOSTAS = '3'
RESULTADO = '4'
LOGOUT = '5'

api_app = API_APP('127.0.0.1', 8888)

# message RESPOSTA {
#   required int32 id = 1;
#   oneof resp {
#     string texto = 2;
#     CODIGOS codigos = 3; // letra da questão, se tiver
#   }
# }
def pegando_respostas():
    r1 = provaonline_pb2.RESPOSTA()
    r1.id = 654
    r1.codigos.codigos.append('222')
    r2 = provaonline_pb2.RESPOSTA()
    r2.id = 987
    r2.codigos.codigos.append('111')
    r3 = provaonline_pb2.RESPOSTA()
    r3.id = 321
    r3.texto = "A Rosa dos Ventos eh um instrumento antigo utilizado para auxiliar na localizacao relativa."
    return [r1, r2, r3]

def menu(switch):
    
    print("------ MENU ------")
    print("1 - Login")
    print("2 - Requisição de prova")
    print("3 - Responder prova")
    print("4 - Resultado da prova")
    print("5 - Logout")
    option = input(">> ")
    switch[option]()

def login():
    print("****** LOGIN *****\n")
    usuario = input("Usuario: ")
    senha = input("Senha: ")
    if api_app.login(usuario, senha):
        print("LOGIN OK")
    else: print("NACK")

def prova():
    print("****** SOLICITA PROVA *****\n")
    idprova = input("ID da prova: ")
    ack, msg = api_app.reqprova(idprova)
    if ack:
        print("REQPROVA OK")
        print(msg)
    else: print("NACK")


def respostas():
    print("****** ENVIA RESPOSTAS *****\n")
    idprova = input("ID da prova: ")
    ack, msg = api_app.reqresp(idprova, pegando_respostas())
    if ack:
        print("REQRESP OK")
    else: print("NACK")

def resultado():
    print("****** SOLICITA RESULTADOS *****\n")
    idprova = input("ID da prova: ")
    if api_app.reqresultado():
        print("REQRESULTADO OK")
    else: print("NACK")


def logout():
    print("***** LOGOUT *****\n")
    if api_app.logout():
        print("LOGOUT OK")
    else: print("NACK")
    

if __name__ == '__main__':
    switch = {
        LOGIN: login,
        PROVA: prova,
        RESPOSTAS: respostas,
        RESULTADO: resultado,
        LOGOUT: logout
    }

    while True:
        menu(switch)
    
    cliente.close()
    