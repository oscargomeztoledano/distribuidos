# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensor.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0csensor.proto\"\x9e\x01\n\x07Reading\x12\n\n\x02Id\x18\x01 \x01(\x05\x12!\n\x04type\x18\x02 \x01(\x0e\x32\x13.Reading.SensorType\x12\r\n\x05value\x18\x03 \x01(\x02\x12\x0c\n\x04unit\x18\x04 \x01(\t\"G\n\nSensorType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08HUMIDITY\x10\x01\x12\x0c\n\x08PRESSURE\x10\x02\x12\x10\n\x0c\x41\x43\x43\x45LERATION\x10\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sensor_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_READING']._serialized_start=17
  _globals['_READING']._serialized_end=175
  _globals['_READING_SENSORTYPE']._serialized_start=104
  _globals['_READING_SENSORTYPE']._serialized_end=175
# @@protoc_insertion_point(module_scope)