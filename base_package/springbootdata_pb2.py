# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: springbootdata.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14springbootdata.proto\x12\x0c\x62\x61se_package\"\'\n\x0bTestRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x18\n\tTestReply\x12\x0b\n\x03res\x18\x01 \x01(\t2U\n\x0fTestGrpcService\x12\x42\n\ntestMethod\x12\x19.base_package.TestRequest\x1a\x17.base_package.TestReply\"\x00\x62\x06proto3')



_TESTREQUEST = DESCRIPTOR.message_types_by_name['TestRequest']
_TESTREPLY = DESCRIPTOR.message_types_by_name['TestReply']
TestRequest = _reflection.GeneratedProtocolMessageType('TestRequest', (_message.Message,), {
  'DESCRIPTOR' : _TESTREQUEST,
  '__module__' : 'springbootdata_pb2'
  # @@protoc_insertion_point(class_scope:base_package.TestRequest)
  })
_sym_db.RegisterMessage(TestRequest)

TestReply = _reflection.GeneratedProtocolMessageType('TestReply', (_message.Message,), {
  'DESCRIPTOR' : _TESTREPLY,
  '__module__' : 'springbootdata_pb2'
  # @@protoc_insertion_point(class_scope:base_package.TestReply)
  })
_sym_db.RegisterMessage(TestReply)

_TESTGRPCSERVICE = DESCRIPTOR.services_by_name['TestGrpcService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TESTREQUEST._serialized_start=38
  _TESTREQUEST._serialized_end=77
  _TESTREPLY._serialized_start=79
  _TESTREPLY._serialized_end=103
  _TESTGRPCSERVICE._serialized_start=105
  _TESTGRPCSERVICE._serialized_end=190
# @@protoc_insertion_point(module_scope)
