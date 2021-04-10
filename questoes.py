#!/usr/bin/python3
 
import provaonline_pb2

ackreqprova = provaonline_pb2.ACK_REQ_PROVA()
ackreqprova.id_prova = '11233'
questao1 = ackreqprova.questoes.add()
questao1.id = 654
questao1.enunciado = 'Qual a capital de Santa Catarina?'
questao1.pontos = 3
alternativa11 = questao1.alternativas.add()
alternativa11.codigo = '111'
alternativa11.descricao = '(a) Sao Paulo'
alternativa12 = questao1.alternativas.add()
alternativa12.codigo = '222'
alternativa12.descricao = '(b) Florianopolis'
alternativa13 = questao1.alternativas.add()
alternativa13.codigo = '333'
alternativa13.descricao = '(c) Sao Paulo'
questao2 = ackreqprova.questoes.add()
questao2.id = 987
questao2.enunciado = 'Qual a capital de Pernambuco?'
questao2.pontos = 3
alternativa21 = questao2.alternativas.add()
alternativa21.codigo = '111'
alternativa21.descricao = '(a) Recife'
alternativa22 = questao2.alternativas.add()
alternativa22.codigo = '222'
alternativa22.descricao = '(b) Aracaju'
alternativa23 = questao2.alternativas.add()
alternativa23.codigo = '333'
alternativa23.descricao = '(c) Goiania'
questao3 = ackreqprova.questoes.add()
questao3.id = 321
questao3.enunciado = 'Qual a utilidade da Rosa dos Ventos?'
questao3.pontos = 4

data4 = ackreqprova.SerializeToString()

# print('Mensagem codificada:', data4)
copia4 = provaonline_pb2.ACK_REQ_PROVA()

# print('Mensagem decodificada:')
# print(ackreqprova)

# Write the new address book back to disk.
f = open('questoes.txt', "wb")
f.write(ackreqprova.SerializeToString())
f.close()