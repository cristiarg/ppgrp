# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proxy.proto',
  package='ppgrp',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0bproxy.proto\x12\x05ppgrp\"-\n\x15ServiceSessionRequest\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\"\x1c\n\x0c\x45ndpointInfo\x12\x0c\n\x04port\x18\x01 \x01(\x05\"c\n\x0bSessionInfo\x12\x12\n\nsession_id\x18\x01 \x01(\x05\x12\x14\n\x0cservice_name\x18\x02 \x01(\t\x12*\n\rendpoint_info\x18\x03 \x01(\x0b\x32\x13.ppgrp.EndpointInfo\"B\n\x16ServiceSessionResponse\x12(\n\x0csession_info\x18\x02 \x01(\x0b\x32\x12.ppgrp.SessionInfo2]\n\x11SessionDispatcher\x12H\n\x07Request\x12\x1c.ppgrp.ServiceSessionRequest\x1a\x1d.ppgrp.ServiceSessionResponse\"\x00\x62\x06proto3')
)




_SERVICESESSIONREQUEST = _descriptor.Descriptor(
  name='ServiceSessionRequest',
  full_name='ppgrp.ServiceSessionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_name', full_name='ppgrp.ServiceSessionRequest.service_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=67,
)


_ENDPOINTINFO = _descriptor.Descriptor(
  name='EndpointInfo',
  full_name='ppgrp.EndpointInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='port', full_name='ppgrp.EndpointInfo.port', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=97,
)


_SESSIONINFO = _descriptor.Descriptor(
  name='SessionInfo',
  full_name='ppgrp.SessionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='ppgrp.SessionInfo.session_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_name', full_name='ppgrp.SessionInfo.service_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endpoint_info', full_name='ppgrp.SessionInfo.endpoint_info', index=2,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=198,
)


_SERVICESESSIONRESPONSE = _descriptor.Descriptor(
  name='ServiceSessionResponse',
  full_name='ppgrp.ServiceSessionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_info', full_name='ppgrp.ServiceSessionResponse.session_info', index=0,
      number=2, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=200,
  serialized_end=266,
)

_SESSIONINFO.fields_by_name['endpoint_info'].message_type = _ENDPOINTINFO
_SERVICESESSIONRESPONSE.fields_by_name['session_info'].message_type = _SESSIONINFO
DESCRIPTOR.message_types_by_name['ServiceSessionRequest'] = _SERVICESESSIONREQUEST
DESCRIPTOR.message_types_by_name['EndpointInfo'] = _ENDPOINTINFO
DESCRIPTOR.message_types_by_name['SessionInfo'] = _SESSIONINFO
DESCRIPTOR.message_types_by_name['ServiceSessionResponse'] = _SERVICESESSIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServiceSessionRequest = _reflection.GeneratedProtocolMessageType('ServiceSessionRequest', (_message.Message,), dict(
  DESCRIPTOR = _SERVICESESSIONREQUEST,
  __module__ = 'proxy_pb2'
  # @@protoc_insertion_point(class_scope:ppgrp.ServiceSessionRequest)
  ))
_sym_db.RegisterMessage(ServiceSessionRequest)

EndpointInfo = _reflection.GeneratedProtocolMessageType('EndpointInfo', (_message.Message,), dict(
  DESCRIPTOR = _ENDPOINTINFO,
  __module__ = 'proxy_pb2'
  # @@protoc_insertion_point(class_scope:ppgrp.EndpointInfo)
  ))
_sym_db.RegisterMessage(EndpointInfo)

SessionInfo = _reflection.GeneratedProtocolMessageType('SessionInfo', (_message.Message,), dict(
  DESCRIPTOR = _SESSIONINFO,
  __module__ = 'proxy_pb2'
  # @@protoc_insertion_point(class_scope:ppgrp.SessionInfo)
  ))
_sym_db.RegisterMessage(SessionInfo)

ServiceSessionResponse = _reflection.GeneratedProtocolMessageType('ServiceSessionResponse', (_message.Message,), dict(
  DESCRIPTOR = _SERVICESESSIONRESPONSE,
  __module__ = 'proxy_pb2'
  # @@protoc_insertion_point(class_scope:ppgrp.ServiceSessionResponse)
  ))
_sym_db.RegisterMessage(ServiceSessionResponse)



_SESSIONDISPATCHER = _descriptor.ServiceDescriptor(
  name='SessionDispatcher',
  full_name='ppgrp.SessionDispatcher',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=268,
  serialized_end=361,
  methods=[
  _descriptor.MethodDescriptor(
    name='Request',
    full_name='ppgrp.SessionDispatcher.Request',
    index=0,
    containing_service=None,
    input_type=_SERVICESESSIONREQUEST,
    output_type=_SERVICESESSIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SESSIONDISPATCHER)

DESCRIPTOR.services_by_name['SessionDispatcher'] = _SESSIONDISPATCHER

# @@protoc_insertion_point(module_scope)
