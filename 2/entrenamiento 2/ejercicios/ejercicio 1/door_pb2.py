# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: door.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ndoor.proto\"\xcf\x01\n\x0e\x43ontrolMessage\x12\n\n\x02id\x18\x01 \x01(\x05\x12(\n\x07\x63ommand\x18\x02 \x01(\x0e\x32\x17.ControlMessage.Command\x12\"\n\x04mode\x18\x03 \x01(\x0e\x32\x14.ControlMessage.Mode\x12\x0c\n\x04time\x18\x04 \x01(\x05\"0\n\x07\x43ommand\x12\x10\n\x0c\x43HECK_STATUS\x10\x00\x12\x08\n\x04OPEN\x10\x01\x12\t\n\x05\x43LOSE\x10\x02\"#\n\x04Mode\x12\x0b\n\x07VEHICLE\x10\x00\x12\x0e\n\nPEDESTRIAN\x10\x01\"\xa3\x01\n\x0fResponseMessage\x12\n\n\x02id\x18\x01 \x01(\x05\x12\'\n\x06result\x18\x02 \x01(\x0e\x32\x17.ResponseMessage.Result\"[\n\x06Result\x12\x06\n\x02OK\x10\x00\x12\x10\n\x0c\x41LREADY_OPEN\x10\x01\x12\x12\n\x0e\x41LREADY_CLOSED\x10\x02\x12\x12\n\x0eOBSTACLE_FOUND\x10\x03\x12\x0f\n\x0bMOTOR_ERROR\x10\x04\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'door_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CONTROLMESSAGE']._serialized_start=15
  _globals['_CONTROLMESSAGE']._serialized_end=222
  _globals['_CONTROLMESSAGE_COMMAND']._serialized_start=137
  _globals['_CONTROLMESSAGE_COMMAND']._serialized_end=185
  _globals['_CONTROLMESSAGE_MODE']._serialized_start=187
  _globals['_CONTROLMESSAGE_MODE']._serialized_end=222
  _globals['_RESPONSEMESSAGE']._serialized_start=225
  _globals['_RESPONSEMESSAGE']._serialized_end=388
  _globals['_RESPONSEMESSAGE_RESULT']._serialized_start=297
  _globals['_RESPONSEMESSAGE_RESULT']._serialized_end=388
# @@protoc_insertion_point(module_scope)