# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: client_login.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Network.ProtoPB2.common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='client_login.proto',
  package='myproto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12\x63lient_login.proto\x12\x07myproto\x1a\x0c\x63ommon.proto\"\t\n\x07PingREQ\"D\n\x07PingACK\x12 \n\x03Ret\x18\x01 \x01(\x0e\x32\x13.myproto.ResultCode\x12\x17\n\x0fServerTimestamp\x18\x02 \x01(\x03\"\x1c\n\tVerifyREQ\x12\x0f\n\x07Version\x18\x01 \x01(\t\"k\n\tVerifyACK\x12 \n\x03Ret\x18\x01 \x01(\x0e\x32\x13.myproto.ResultCode\x12\x10\n\x08\x43lientIp\x18\x02 \x01(\t\x12\x16\n\x0eTimeZoneOffset\x18\x04 \x01(\x05\x12\x12\n\nEncryptKey\x18\x05 \x01(\x0c\"1\n\x0c\x45nterGameREQ\x12\x0f\n\x07\x41\x63\x63ount\x18\x01 \x01(\t\x12\x10\n\x08Password\x18\x02 \x01(\t\"D\n\x0c\x45nterGameACK\x12 \n\x03Ret\x18\x01 \x01(\x0e\x32\x13.myproto.ResultCode\x12\x12\n\nServerList\x18\x02 \x03(\x05\"#\n\x0fSelectServerREQ\x12\x10\n\x08ServerId\x18\x01 \x01(\x05\"E\n\x0fSelectServerACK\x12 \n\x03Ret\x18\x01 \x01(\x0e\x32\x13.myproto.ResultCode\x12\x10\n\x08RoleList\x18\x02 \x03(\x05\x62\x06proto3'
  ,
  dependencies=[common__pb2.DESCRIPTOR,])




_PINGREQ = _descriptor.Descriptor(
  name='PingREQ',
  full_name='myproto.PingREQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=54,
)


_PINGACK = _descriptor.Descriptor(
  name='PingACK',
  full_name='myproto.PingACK',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Ret', full_name='myproto.PingACK.Ret', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ServerTimestamp', full_name='myproto.PingACK.ServerTimestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=124,
)


_VERIFYREQ = _descriptor.Descriptor(
  name='VerifyREQ',
  full_name='myproto.VerifyREQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Version', full_name='myproto.VerifyREQ.Version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=154,
)


_VERIFYACK = _descriptor.Descriptor(
  name='VerifyACK',
  full_name='myproto.VerifyACK',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Ret', full_name='myproto.VerifyACK.Ret', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ClientIp', full_name='myproto.VerifyACK.ClientIp', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='TimeZoneOffset', full_name='myproto.VerifyACK.TimeZoneOffset', index=2,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='EncryptKey', full_name='myproto.VerifyACK.EncryptKey', index=3,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=156,
  serialized_end=263,
)


_ENTERGAMEREQ = _descriptor.Descriptor(
  name='EnterGameREQ',
  full_name='myproto.EnterGameREQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Account', full_name='myproto.EnterGameREQ.Account', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Password', full_name='myproto.EnterGameREQ.Password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=265,
  serialized_end=314,
)


_ENTERGAMEACK = _descriptor.Descriptor(
  name='EnterGameACK',
  full_name='myproto.EnterGameACK',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Ret', full_name='myproto.EnterGameACK.Ret', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ServerList', full_name='myproto.EnterGameACK.ServerList', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=316,
  serialized_end=384,
)


_SELECTSERVERREQ = _descriptor.Descriptor(
  name='SelectServerREQ',
  full_name='myproto.SelectServerREQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ServerId', full_name='myproto.SelectServerREQ.ServerId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=386,
  serialized_end=421,
)


_SELECTSERVERACK = _descriptor.Descriptor(
  name='SelectServerACK',
  full_name='myproto.SelectServerACK',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Ret', full_name='myproto.SelectServerACK.Ret', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='RoleList', full_name='myproto.SelectServerACK.RoleList', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=423,
  serialized_end=492,
)

_PINGACK.fields_by_name['Ret'].enum_type = common__pb2._RESULTCODE
_VERIFYACK.fields_by_name['Ret'].enum_type = common__pb2._RESULTCODE
_ENTERGAMEACK.fields_by_name['Ret'].enum_type = common__pb2._RESULTCODE
_SELECTSERVERACK.fields_by_name['Ret'].enum_type = common__pb2._RESULTCODE
DESCRIPTOR.message_types_by_name['PingREQ'] = _PINGREQ
DESCRIPTOR.message_types_by_name['PingACK'] = _PINGACK
DESCRIPTOR.message_types_by_name['VerifyREQ'] = _VERIFYREQ
DESCRIPTOR.message_types_by_name['VerifyACK'] = _VERIFYACK
DESCRIPTOR.message_types_by_name['EnterGameREQ'] = _ENTERGAMEREQ
DESCRIPTOR.message_types_by_name['EnterGameACK'] = _ENTERGAMEACK
DESCRIPTOR.message_types_by_name['SelectServerREQ'] = _SELECTSERVERREQ
DESCRIPTOR.message_types_by_name['SelectServerACK'] = _SELECTSERVERACK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PingREQ = _reflection.GeneratedProtocolMessageType('PingREQ', (_message.Message,), {
  'DESCRIPTOR' : _PINGREQ,
  '__module__' : 'client_login_pb2'
  # @@protoc_insertion_point(class_scope:myproto.PingREQ)
  })
_sym_db.RegisterMessage(PingREQ)

PingACK = _reflection.GeneratedProtocolMessageType('PingACK', (_message.Message,), {
  'DESCRIPTOR' : _PINGACK,
  '__module__' : 'client_login_pb2'
  # @@protoc_insertion_point(class_scope:myproto.PingACK)
  })
_sym_db.RegisterMessage(PingACK)

VerifyREQ = _reflection.GeneratedProtocolMessageType('VerifyREQ', (_message.Message,), {
  'DESCRIPTOR' : _VERIFYREQ,
  '__module__' : 'client_login_pb2'
  # @@protoc_insertion_point(class_scope:myproto.VerifyREQ)
  })
_sym_db.RegisterMessage(VerifyREQ)

VerifyACK = _reflection.GeneratedProtocolMessageType('VerifyACK', (_message.Message,), {
  'DESCRIPTOR' : _VERIFYACK,
  '__module__' : 'client_login_pb2'
  # @@protoc_insertion_point(class_scope:myproto.VerifyACK)
  })
_sym_db.RegisterMessage(VerifyACK)

EnterGameREQ = _reflection.GeneratedProtocolMessageType('EnterGameREQ', (_message.Message,), {
  'DESCRIPTOR' : _ENTERGAMEREQ,
  '__module__' : 'client_login_pb2'
  # @@protoc_insertion_point(class_scope:myproto.EnterGameREQ)
  })
_sym_db.RegisterMessage(EnterGameREQ)

EnterGameACK = _reflection.GeneratedProtocolMessageType('EnterGameACK', (_message.Message,), {
  'DESCRIPTOR' : _ENTERGAMEACK,
  '__module__' : 'client_login_pb2'
  # @@protoc_insertion_point(class_scope:myproto.EnterGameACK)
  })
_sym_db.RegisterMessage(EnterGameACK)

SelectServerREQ = _reflection.GeneratedProtocolMessageType('SelectServerREQ', (_message.Message,), {
  'DESCRIPTOR' : _SELECTSERVERREQ,
  '__module__' : 'client_login_pb2'
  # @@protoc_insertion_point(class_scope:myproto.SelectServerREQ)
  })
_sym_db.RegisterMessage(SelectServerREQ)

SelectServerACK = _reflection.GeneratedProtocolMessageType('SelectServerACK', (_message.Message,), {
  'DESCRIPTOR' : _SELECTSERVERACK,
  '__module__' : 'client_login_pb2'
  # @@protoc_insertion_point(class_scope:myproto.SelectServerACK)
  })
_sym_db.RegisterMessage(SelectServerACK)


# @@protoc_insertion_point(module_scope)
