# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common.proto',
  package='myproto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x63ommon.proto\x12\x07myproto*\x19\n\nResultCode\x12\x0b\n\x07NoError\x10\x00\x62\x06proto3'
)

_RESULTCODE = _descriptor.EnumDescriptor(
  name='ResultCode',
  full_name='myproto.ResultCode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NoError', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=25,
  serialized_end=50,
)
_sym_db.RegisterEnumDescriptor(_RESULTCODE)

ResultCode = enum_type_wrapper.EnumTypeWrapper(_RESULTCODE)
NoError = 0


DESCRIPTOR.enum_types_by_name['ResultCode'] = _RESULTCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)