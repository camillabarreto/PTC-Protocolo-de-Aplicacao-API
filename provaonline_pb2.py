# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: provaonline.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='provaonline.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x11provaonline.proto\"\xbc\x02\n\x08MENSAGEM\x12\x17\n\x05login\x18\x01 \x01(\x0b\x32\x06.LOGINH\x00\x12\x19\n\x06logout\x18\x02 \x01(\x0b\x32\x07.LOGOUTH\x00\x12\x1e\n\x08\x61\x63klogin\x18\x03 \x01(\x0b\x32\n.ACK_LOGINH\x00\x12\x19\n\x06status\x18\x04 \x01(\x0b\x32\x07.STATUSH\x00\x12\x1e\n\x08reqprova\x18\x05 \x01(\x0b\x32\n.REQ_PROVAH\x00\x12%\n\x0b\x61\x63kreqprova\x18\x06 \x01(\x0b\x32\x0e.ACK_REQ_PROVAH\x00\x12&\n\x0creqresultado\x18\x07 \x01(\x0b\x32\x0e.REQ_RESULTADOH\x00\x12-\n\x0f\x61\x63kreqresultado\x18\x08 \x01(\x0b\x32\x12.ACK_REQ_RESULTADOH\x00\x12\x1c\n\x07reqresp\x18\t \x01(\x0b\x32\t.REQ_RESPH\x00\x42\x05\n\x03msg\"%\n\x05LOGIN\x12\r\n\x05login\x18\x01 \x02(\t\x12\r\n\x05senha\x18\x02 \x02(\t\"3\n\tACK_LOGIN\x12\r\n\x05token\x18\x01 \x01(\t\x12\x17\n\x06status\x18\x02 \x02(\x0b\x32\x07.STATUS\"+\n\x06STATUS\x12\x0e\n\x06\x63odigo\x18\x01 \x02(\x05\x12\x11\n\tdescricao\x18\x02 \x01(\t\",\n\tREQ_PROVA\x12\r\n\x05token\x18\x01 \x02(\t\x12\x10\n\x08id_prova\x18\x02 \x01(\t\"0\n\x0b\x41LTERNATIVA\x12\x11\n\tdescricao\x18\x01 \x02(\t\x12\x0e\n\x06\x63odigo\x18\x02 \x02(\t\"\\\n\x07QUESTAO\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x11\n\tenunciado\x18\x02 \x02(\t\x12\x0e\n\x06pontos\x18\x03 \x01(\x05\x12\"\n\x0c\x61lternativas\x18\x04 \x03(\x0b\x32\x0c.ALTERNATIVA\"=\n\rACK_REQ_PROVA\x12\x10\n\x08id_prova\x18\x01 \x02(\t\x12\x1a\n\x08questoes\x18\x02 \x03(\x0b\x32\x08.QUESTAO\"\x1a\n\x07\x43ODIGOS\x12\x0f\n\x07\x63odigos\x18\x01 \x03(\t\"L\n\x08RESPOSTA\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0f\n\x05texto\x18\x02 \x01(\tH\x00\x12\x1b\n\x07\x63odigos\x18\x03 \x01(\x0b\x32\x08.CODIGOSH\x00\x42\x06\n\x04resp\"I\n\x08REQ_RESP\x12\r\n\x05token\x18\x01 \x02(\t\x12\x10\n\x08id_prova\x18\x02 \x02(\t\x12\x1c\n\trespostas\x18\x03 \x03(\x0b\x32\t.RESPOSTA\"0\n\rREQ_RESULTADO\x12\r\n\x05token\x18\x01 \x02(\t\x12\x10\n\x08id_prova\x18\x02 \x02(\t\",\n\tRESULTADO\x12\x0f\n\x07questao\x18\x01 \x02(\x05\x12\x0e\n\x06pontos\x18\x02 \x02(\x05\"Q\n\x11\x41\x43K_REQ_RESULTADO\x12\x10\n\x08id_prova\x18\x01 \x02(\t\x12\x0c\n\x04nota\x18\x02 \x02(\x05\x12\x1c\n\x08questoes\x18\x03 \x03(\x0b\x32\n.RESULTADO\"\x17\n\x06LOGOUT\x12\r\n\x05token\x18\x01 \x02(\t')
)




_MENSAGEM = _descriptor.Descriptor(
  name='MENSAGEM',
  full_name='MENSAGEM',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='login', full_name='MENSAGEM.login', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logout', full_name='MENSAGEM.logout', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acklogin', full_name='MENSAGEM.acklogin', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='MENSAGEM.status', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reqprova', full_name='MENSAGEM.reqprova', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ackreqprova', full_name='MENSAGEM.ackreqprova', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reqresultado', full_name='MENSAGEM.reqresultado', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ackreqresultado', full_name='MENSAGEM.ackreqresultado', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reqresp', full_name='MENSAGEM.reqresp', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='msg', full_name='MENSAGEM.msg',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=22,
  serialized_end=338,
)


_LOGIN = _descriptor.Descriptor(
  name='LOGIN',
  full_name='LOGIN',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='login', full_name='LOGIN.login', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='senha', full_name='LOGIN.senha', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=340,
  serialized_end=377,
)


_ACK_LOGIN = _descriptor.Descriptor(
  name='ACK_LOGIN',
  full_name='ACK_LOGIN',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='ACK_LOGIN.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='ACK_LOGIN.status', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=379,
  serialized_end=430,
)


_STATUS = _descriptor.Descriptor(
  name='STATUS',
  full_name='STATUS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='codigo', full_name='STATUS.codigo', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='descricao', full_name='STATUS.descricao', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=432,
  serialized_end=475,
)


_REQ_PROVA = _descriptor.Descriptor(
  name='REQ_PROVA',
  full_name='REQ_PROVA',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='REQ_PROVA.token', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id_prova', full_name='REQ_PROVA.id_prova', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=477,
  serialized_end=521,
)


_ALTERNATIVA = _descriptor.Descriptor(
  name='ALTERNATIVA',
  full_name='ALTERNATIVA',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='descricao', full_name='ALTERNATIVA.descricao', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codigo', full_name='ALTERNATIVA.codigo', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=523,
  serialized_end=571,
)


_QUESTAO = _descriptor.Descriptor(
  name='QUESTAO',
  full_name='QUESTAO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='QUESTAO.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enunciado', full_name='QUESTAO.enunciado', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pontos', full_name='QUESTAO.pontos', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alternativas', full_name='QUESTAO.alternativas', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=573,
  serialized_end=665,
)


_ACK_REQ_PROVA = _descriptor.Descriptor(
  name='ACK_REQ_PROVA',
  full_name='ACK_REQ_PROVA',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id_prova', full_name='ACK_REQ_PROVA.id_prova', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='questoes', full_name='ACK_REQ_PROVA.questoes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=667,
  serialized_end=728,
)


_CODIGOS = _descriptor.Descriptor(
  name='CODIGOS',
  full_name='CODIGOS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='codigos', full_name='CODIGOS.codigos', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=730,
  serialized_end=756,
)


_RESPOSTA = _descriptor.Descriptor(
  name='RESPOSTA',
  full_name='RESPOSTA',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='RESPOSTA.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='texto', full_name='RESPOSTA.texto', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codigos', full_name='RESPOSTA.codigos', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='resp', full_name='RESPOSTA.resp',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=758,
  serialized_end=834,
)


_REQ_RESP = _descriptor.Descriptor(
  name='REQ_RESP',
  full_name='REQ_RESP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='REQ_RESP.token', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id_prova', full_name='REQ_RESP.id_prova', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='respostas', full_name='REQ_RESP.respostas', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=836,
  serialized_end=909,
)


_REQ_RESULTADO = _descriptor.Descriptor(
  name='REQ_RESULTADO',
  full_name='REQ_RESULTADO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='REQ_RESULTADO.token', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id_prova', full_name='REQ_RESULTADO.id_prova', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=911,
  serialized_end=959,
)


_RESULTADO = _descriptor.Descriptor(
  name='RESULTADO',
  full_name='RESULTADO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='questao', full_name='RESULTADO.questao', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pontos', full_name='RESULTADO.pontos', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=961,
  serialized_end=1005,
)


_ACK_REQ_RESULTADO = _descriptor.Descriptor(
  name='ACK_REQ_RESULTADO',
  full_name='ACK_REQ_RESULTADO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id_prova', full_name='ACK_REQ_RESULTADO.id_prova', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nota', full_name='ACK_REQ_RESULTADO.nota', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='questoes', full_name='ACK_REQ_RESULTADO.questoes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1007,
  serialized_end=1088,
)


_LOGOUT = _descriptor.Descriptor(
  name='LOGOUT',
  full_name='LOGOUT',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='LOGOUT.token', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1090,
  serialized_end=1113,
)

_MENSAGEM.fields_by_name['login'].message_type = _LOGIN
_MENSAGEM.fields_by_name['logout'].message_type = _LOGOUT
_MENSAGEM.fields_by_name['acklogin'].message_type = _ACK_LOGIN
_MENSAGEM.fields_by_name['status'].message_type = _STATUS
_MENSAGEM.fields_by_name['reqprova'].message_type = _REQ_PROVA
_MENSAGEM.fields_by_name['ackreqprova'].message_type = _ACK_REQ_PROVA
_MENSAGEM.fields_by_name['reqresultado'].message_type = _REQ_RESULTADO
_MENSAGEM.fields_by_name['ackreqresultado'].message_type = _ACK_REQ_RESULTADO
_MENSAGEM.fields_by_name['reqresp'].message_type = _REQ_RESP
_MENSAGEM.oneofs_by_name['msg'].fields.append(
  _MENSAGEM.fields_by_name['login'])
_MENSAGEM.fields_by_name['login'].containing_oneof = _MENSAGEM.oneofs_by_name['msg']
_MENSAGEM.oneofs_by_name['msg'].fields.append(
  _MENSAGEM.fields_by_name['logout'])
_MENSAGEM.fields_by_name['logout'].containing_oneof = _MENSAGEM.oneofs_by_name['msg']
_MENSAGEM.oneofs_by_name['msg'].fields.append(
  _MENSAGEM.fields_by_name['acklogin'])
_MENSAGEM.fields_by_name['acklogin'].containing_oneof = _MENSAGEM.oneofs_by_name['msg']
_MENSAGEM.oneofs_by_name['msg'].fields.append(
  _MENSAGEM.fields_by_name['status'])
_MENSAGEM.fields_by_name['status'].containing_oneof = _MENSAGEM.oneofs_by_name['msg']
_MENSAGEM.oneofs_by_name['msg'].fields.append(
  _MENSAGEM.fields_by_name['reqprova'])
_MENSAGEM.fields_by_name['reqprova'].containing_oneof = _MENSAGEM.oneofs_by_name['msg']
_MENSAGEM.oneofs_by_name['msg'].fields.append(
  _MENSAGEM.fields_by_name['ackreqprova'])
_MENSAGEM.fields_by_name['ackreqprova'].containing_oneof = _MENSAGEM.oneofs_by_name['msg']
_MENSAGEM.oneofs_by_name['msg'].fields.append(
  _MENSAGEM.fields_by_name['reqresultado'])
_MENSAGEM.fields_by_name['reqresultado'].containing_oneof = _MENSAGEM.oneofs_by_name['msg']
_MENSAGEM.oneofs_by_name['msg'].fields.append(
  _MENSAGEM.fields_by_name['ackreqresultado'])
_MENSAGEM.fields_by_name['ackreqresultado'].containing_oneof = _MENSAGEM.oneofs_by_name['msg']
_MENSAGEM.oneofs_by_name['msg'].fields.append(
  _MENSAGEM.fields_by_name['reqresp'])
_MENSAGEM.fields_by_name['reqresp'].containing_oneof = _MENSAGEM.oneofs_by_name['msg']
_ACK_LOGIN.fields_by_name['status'].message_type = _STATUS
_QUESTAO.fields_by_name['alternativas'].message_type = _ALTERNATIVA
_ACK_REQ_PROVA.fields_by_name['questoes'].message_type = _QUESTAO
_RESPOSTA.fields_by_name['codigos'].message_type = _CODIGOS
_RESPOSTA.oneofs_by_name['resp'].fields.append(
  _RESPOSTA.fields_by_name['texto'])
_RESPOSTA.fields_by_name['texto'].containing_oneof = _RESPOSTA.oneofs_by_name['resp']
_RESPOSTA.oneofs_by_name['resp'].fields.append(
  _RESPOSTA.fields_by_name['codigos'])
_RESPOSTA.fields_by_name['codigos'].containing_oneof = _RESPOSTA.oneofs_by_name['resp']
_REQ_RESP.fields_by_name['respostas'].message_type = _RESPOSTA
_ACK_REQ_RESULTADO.fields_by_name['questoes'].message_type = _RESULTADO
DESCRIPTOR.message_types_by_name['MENSAGEM'] = _MENSAGEM
DESCRIPTOR.message_types_by_name['LOGIN'] = _LOGIN
DESCRIPTOR.message_types_by_name['ACK_LOGIN'] = _ACK_LOGIN
DESCRIPTOR.message_types_by_name['STATUS'] = _STATUS
DESCRIPTOR.message_types_by_name['REQ_PROVA'] = _REQ_PROVA
DESCRIPTOR.message_types_by_name['ALTERNATIVA'] = _ALTERNATIVA
DESCRIPTOR.message_types_by_name['QUESTAO'] = _QUESTAO
DESCRIPTOR.message_types_by_name['ACK_REQ_PROVA'] = _ACK_REQ_PROVA
DESCRIPTOR.message_types_by_name['CODIGOS'] = _CODIGOS
DESCRIPTOR.message_types_by_name['RESPOSTA'] = _RESPOSTA
DESCRIPTOR.message_types_by_name['REQ_RESP'] = _REQ_RESP
DESCRIPTOR.message_types_by_name['REQ_RESULTADO'] = _REQ_RESULTADO
DESCRIPTOR.message_types_by_name['RESULTADO'] = _RESULTADO
DESCRIPTOR.message_types_by_name['ACK_REQ_RESULTADO'] = _ACK_REQ_RESULTADO
DESCRIPTOR.message_types_by_name['LOGOUT'] = _LOGOUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MENSAGEM = _reflection.GeneratedProtocolMessageType('MENSAGEM', (_message.Message,), dict(
  DESCRIPTOR = _MENSAGEM,
  __module__ = 'provaonline_pb2'
  # @@protoc_insertion_point(class_scope:MENSAGEM)
  ))
_sym_db.RegisterMessage(MENSAGEM)

LOGIN = _reflection.GeneratedProtocolMessageType('LOGIN', (_message.Message,), dict(
  DESCRIPTOR = _LOGIN,
  __module__ = 'provaonline_pb2'
  # @@protoc_insertion_point(class_scope:LOGIN)
  ))
_sym_db.RegisterMessage(LOGIN)

ACK_LOGIN = _reflection.GeneratedProtocolMessageType('ACK_LOGIN', (_message.Message,), dict(
  DESCRIPTOR = _ACK_LOGIN,
  __module__ = 'provaonline_pb2'
  # @@protoc_insertion_point(class_scope:ACK_LOGIN)
  ))
_sym_db.RegisterMessage(ACK_LOGIN)

STATUS = _reflection.GeneratedProtocolMessageType('STATUS', (_message.Message,), dict(
  DESCRIPTOR = _STATUS,
  __module__ = 'provaonline_pb2'
  # @@protoc_insertion_point(class_scope:STATUS)
  ))
_sym_db.RegisterMessage(STATUS)

REQ_PROVA = _reflection.GeneratedProtocolMessageType('REQ_PROVA', (_message.Message,), dict(
  DESCRIPTOR = _REQ_PROVA,
  __module__ = 'provaonline_pb2'
  # @@protoc_insertion_point(class_scope:REQ_PROVA)
  ))
_sym_db.RegisterMessage(REQ_PROVA)

ALTERNATIVA = _reflection.GeneratedProtocolMessageType('ALTERNATIVA', (_message.Message,), dict(
  DESCRIPTOR = _ALTERNATIVA,
  __module__ = 'provaonline_pb2'
  # @@protoc_insertion_point(class_scope:ALTERNATIVA)
  ))
_sym_db.RegisterMessage(ALTERNATIVA)

QUESTAO = _reflection.GeneratedProtocolMessageType('QUESTAO', (_message.Message,), dict(
  DESCRIPTOR = _QUESTAO,
  __module__ = 'provaonline_pb2'
  # @@protoc_insertion_point(class_scope:QUESTAO)
  ))
_sym_db.RegisterMessage(QUESTAO)

ACK_REQ_PROVA = _reflection.GeneratedProtocolMessageType('ACK_REQ_PROVA', (_message.Message,), dict(
  DESCRIPTOR = _ACK_REQ_PROVA,
  __module__ = 'provaonline_pb2'
  # @@protoc_insertion_point(class_scope:ACK_REQ_PROVA)
  ))
_sym_db.RegisterMessage(ACK_REQ_PROVA)

CODIGOS = _reflection.GeneratedProtocolMessageType('CODIGOS', (_message.Message,), dict(
  DESCRIPTOR = _CODIGOS,
  __module__ = 'provaonline_pb2'
  # @@protoc_insertion_point(class_scope:CODIGOS)
  ))
_sym_db.RegisterMessage(CODIGOS)

RESPOSTA = _reflection.GeneratedProtocolMessageType('RESPOSTA', (_message.Message,), dict(
  DESCRIPTOR = _RESPOSTA,
  __module__ = 'provaonline_pb2'
  # @@protoc_insertion_point(class_scope:RESPOSTA)
  ))
_sym_db.RegisterMessage(RESPOSTA)

REQ_RESP = _reflection.GeneratedProtocolMessageType('REQ_RESP', (_message.Message,), dict(
  DESCRIPTOR = _REQ_RESP,
  __module__ = 'provaonline_pb2'
  # @@protoc_insertion_point(class_scope:REQ_RESP)
  ))
_sym_db.RegisterMessage(REQ_RESP)

REQ_RESULTADO = _reflection.GeneratedProtocolMessageType('REQ_RESULTADO', (_message.Message,), dict(
  DESCRIPTOR = _REQ_RESULTADO,
  __module__ = 'provaonline_pb2'
  # @@protoc_insertion_point(class_scope:REQ_RESULTADO)
  ))
_sym_db.RegisterMessage(REQ_RESULTADO)

RESULTADO = _reflection.GeneratedProtocolMessageType('RESULTADO', (_message.Message,), dict(
  DESCRIPTOR = _RESULTADO,
  __module__ = 'provaonline_pb2'
  # @@protoc_insertion_point(class_scope:RESULTADO)
  ))
_sym_db.RegisterMessage(RESULTADO)

ACK_REQ_RESULTADO = _reflection.GeneratedProtocolMessageType('ACK_REQ_RESULTADO', (_message.Message,), dict(
  DESCRIPTOR = _ACK_REQ_RESULTADO,
  __module__ = 'provaonline_pb2'
  # @@protoc_insertion_point(class_scope:ACK_REQ_RESULTADO)
  ))
_sym_db.RegisterMessage(ACK_REQ_RESULTADO)

LOGOUT = _reflection.GeneratedProtocolMessageType('LOGOUT', (_message.Message,), dict(
  DESCRIPTOR = _LOGOUT,
  __module__ = 'provaonline_pb2'
  # @@protoc_insertion_point(class_scope:LOGOUT)
  ))
_sym_db.RegisterMessage(LOGOUT)


# @@protoc_insertion_point(module_scope)