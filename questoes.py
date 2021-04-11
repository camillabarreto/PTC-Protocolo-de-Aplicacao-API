#!/usr/bin/python3
 
import provaonline_pb2

questao1 = provaonline_pb2.QUESTAO()
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

f = open('questao1.txt', "wb")
f.write(questao1.SerializeToString())
f.close()

questao2 = provaonline_pb2.QUESTAO()
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

f = open('questao2.txt', "wb")
f.write(questao2.SerializeToString())
f.close()

questao3 = provaonline_pb2.QUESTAO()
questao3.id = 321
questao3.enunciado = 'Qual a utilidade da Rosa dos Ventos?'
questao3.pontos = 4

f = open('questao3.txt', "wb")
f.write(questao3.SerializeToString())
f.close()