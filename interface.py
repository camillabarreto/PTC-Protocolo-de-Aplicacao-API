#!/usr/bin/env python3

from cliente import Cliente

LOGIN = '1'
PROVA = '2'
RESPOSTAS = '3'
RESULTADO = '4'
LOGOUT = '5'

cliente = None

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
    login = input("Login: ")
    senha = input("Senha: ")
    global cliente
    cliente = Cliente(login, senha)
    cliente.login()

def prova():
    print("****** SOLICITA PROVA *****\n")
    idprova = input("ID da prova: ")
    cliente.reqprova(idprova)

def respostas():
    print("respostas")
    idprova = input("ID da prova: ")

def resultado():
    print("resultado")
    idprova = input("ID da prova: ")
    cliente.reqresultado(id_prova)

def logout():
    print("***** LOGOUT *****\n")
    print('usuario: ', cliente.usuario)
    print('senha: ', cliente.senha)
    print('token: ', cliente.token)
    
    cliente.logout()
    

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
    