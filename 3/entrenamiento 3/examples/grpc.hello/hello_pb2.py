# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hello.proto',
  package='hello',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bhello.proto\x12\x05hello\"\x1f\n\x0cPrintRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x0c\n\nPrintReply2:\n\x05Hello\x12\x31\n\x05write\x12\x13.hello.PrintRequest\x1a\x11.hello.PrintReply\"\x00\x62\x06proto3'
)




_PRINTREQUEST = _descriptor.Descriptor(
  name='PrintRequest',
  full_name='hello.PrintRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='hello.PrintRequest.message', index=0,
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
  serialized_start=22,
  serialized_end=53,
)


_PRINTREPLY = _descriptor.Descriptor(
  name='PrintReply',
  full_name='hello.PrintReply',
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
  serialized_start=55,
  serialized_end=67,
)

DESCRIPTOR.message_types_by_name['PrintRequest'] = _PRINTREQUEST
DESCRIPTOR.message_types_by_name['PrintReply'] = _PRINTREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PrintRequest = _reflection.GeneratedProtocolMessageType('PrintRequest', (_message.Message,), {
  'DESCRIPTOR' : _PRINTREQUEST,
  '__module__' : 'hello_pb2'
  # @@protoc_insertion_point(class_scope:hello.PrintRequest)
  })
_sym_db.RegisterMessage(PrintRequest)

PrintReply = _reflection.GeneratedProtocolMessageType('PrintReply', (_message.Message,), {
  'DESCRIPTOR' : _PRINTREPLY,
  '__module__' : 'hello_pb2'
  # @@protoc_insertion_point(class_scope:hello.PrintReply)
  })
_sym_db.RegisterMessage(PrintReply)



_HELLO = _descriptor.ServiceDescriptor(
  name='Hello',
  full_name='hello.Hello',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=69,
  serialized_end=127,
  methods=[
  _descriptor.MethodDescriptor(
    name='write',
    full_name='hello.Hello.write',
    index=0,
    containing_service=None,
    input_type=_PRINTREQUEST,
    output_type=_PRINTREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_HELLO)

DESCRIPTOR.services_by_name['Hello'] = _HELLO

# @@protoc_insertion_point(module_scope)
