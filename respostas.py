#!/usr/bin/python3
 
import provaonline_pb2

resp1 = provaonline_pb2.RESPOSTA()
resp1.id = 654
cod1 = resp1.codigos.add()
cod1 = '222'

resp2 = provaonline_pb2.RESPOSTA()
resp2.id = 987
cod2 = resp2.codigos.add()
cod2 = '111'

data = ackreqprova.SerializeToString()

# Write the new address book back to disk.
f = open('questoes.txt', "wb")
f.write(ackreqprova.SerializeToString())
f.close()