# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mads.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mads.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nmads.proto\"\"\n\x06Object\x12\x0b\n\x03oid\x18\x01 \x01(\x03\x12\x0b\n\x03URI\x18\x02 \x01(\t\"\x12\n\x03Tag\x12\x0b\n\x03tid\x18\x01 \x01(\x03\"&\n\x17UserCreateObjectRequest\x12\x0b\n\x03URI\x18\x01 \x01(\t\"3\n\x18UserCreateObjectResponse\x12\x17\n\x06object\x18\x01 \x01(\x0b\x32\x07.Object\"O\n\x1ePluginCreateDescriptionRequest\x12\x0b\n\x03oid\x18\x01 \x01(\x03\x12\x0b\n\x03URI\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"4\n\x1fPluginCreateDescriptionResponse\x12\x11\n\x03tag\x18\x01 \x01(\x0b\x32\x04.Tag\"E\n!PluginTranslateDescriptionRequest\x12\x0b\n\x03oid\x18\x01 \x01(\x03\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"7\n\"PluginTranslateDescriptionResponse\x12\x11\n\x03tag\x18\x01 \x01(\x0b\x32\x04.Tag\"]\n\x1cPluginExtractExifDataRequest\x12\x0b\n\x03oid\x18\x01 \x01(\x03\x12\x0b\n\x03URI\x18\x02 \x01(\t\x12\x10\n\x08latitude\x18\x03 \x01(\x02\x12\x11\n\tlongitude\x18\x04 \x01(\x02\"2\n\x1dPluginExtractExifDataResponse\x12\x11\n\x03tag\x18\x01 \x01(\x0b\x32\x04.Tag2\xf4\x02\n\x0cmads_service\x12G\n\x10userCreateObject\x12\x18.UserCreateObjectRequest\x1a\x19.UserCreateObjectResponse\x12\\\n\x17pluginCreateDescription\x12\x1f.PluginCreateDescriptionRequest\x1a .PluginCreateDescriptionResponse\x12\x65\n\x1apluginTranslateDescription\x12\".PluginTranslateDescriptionRequest\x1a#.PluginTranslateDescriptionResponse\x12V\n\x15pluginExtractExifData\x12\x1d.PluginExtractExifDataRequest\x1a\x1e.PluginExtractExifDataResponseb\x06proto3'
)




_OBJECT = _descriptor.Descriptor(
  name='Object',
  full_name='Object',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='oid', full_name='Object.oid', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='URI', full_name='Object.URI', index=1,
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
  serialized_start=14,
  serialized_end=48,
)


_TAG = _descriptor.Descriptor(
  name='Tag',
  full_name='Tag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tid', full_name='Tag.tid', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=50,
  serialized_end=68,
)


_USERCREATEOBJECTREQUEST = _descriptor.Descriptor(
  name='UserCreateObjectRequest',
  full_name='UserCreateObjectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='URI', full_name='UserCreateObjectRequest.URI', index=0,
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
  serialized_start=70,
  serialized_end=108,
)


_USERCREATEOBJECTRESPONSE = _descriptor.Descriptor(
  name='UserCreateObjectResponse',
  full_name='UserCreateObjectResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='object', full_name='UserCreateObjectResponse.object', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=110,
  serialized_end=161,
)


_PLUGINCREATEDESCRIPTIONREQUEST = _descriptor.Descriptor(
  name='PluginCreateDescriptionRequest',
  full_name='PluginCreateDescriptionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='oid', full_name='PluginCreateDescriptionRequest.oid', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='URI', full_name='PluginCreateDescriptionRequest.URI', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='PluginCreateDescriptionRequest.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=163,
  serialized_end=242,
)


_PLUGINCREATEDESCRIPTIONRESPONSE = _descriptor.Descriptor(
  name='PluginCreateDescriptionResponse',
  full_name='PluginCreateDescriptionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='PluginCreateDescriptionResponse.tag', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=244,
  serialized_end=296,
)


_PLUGINTRANSLATEDESCRIPTIONREQUEST = _descriptor.Descriptor(
  name='PluginTranslateDescriptionRequest',
  full_name='PluginTranslateDescriptionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='oid', full_name='PluginTranslateDescriptionRequest.oid', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='PluginTranslateDescriptionRequest.description', index=1,
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
  serialized_start=298,
  serialized_end=367,
)


_PLUGINTRANSLATEDESCRIPTIONRESPONSE = _descriptor.Descriptor(
  name='PluginTranslateDescriptionResponse',
  full_name='PluginTranslateDescriptionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='PluginTranslateDescriptionResponse.tag', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=369,
  serialized_end=424,
)


_PLUGINEXTRACTEXIFDATAREQUEST = _descriptor.Descriptor(
  name='PluginExtractExifDataRequest',
  full_name='PluginExtractExifDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='oid', full_name='PluginExtractExifDataRequest.oid', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='URI', full_name='PluginExtractExifDataRequest.URI', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='PluginExtractExifDataRequest.latitude', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='PluginExtractExifDataRequest.longitude', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=426,
  serialized_end=519,
)


_PLUGINEXTRACTEXIFDATARESPONSE = _descriptor.Descriptor(
  name='PluginExtractExifDataResponse',
  full_name='PluginExtractExifDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='PluginExtractExifDataResponse.tag', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=521,
  serialized_end=571,
)

_USERCREATEOBJECTRESPONSE.fields_by_name['object'].message_type = _OBJECT
_PLUGINCREATEDESCRIPTIONRESPONSE.fields_by_name['tag'].message_type = _TAG
_PLUGINTRANSLATEDESCRIPTIONRESPONSE.fields_by_name['tag'].message_type = _TAG
_PLUGINEXTRACTEXIFDATARESPONSE.fields_by_name['tag'].message_type = _TAG
DESCRIPTOR.message_types_by_name['Object'] = _OBJECT
DESCRIPTOR.message_types_by_name['Tag'] = _TAG
DESCRIPTOR.message_types_by_name['UserCreateObjectRequest'] = _USERCREATEOBJECTREQUEST
DESCRIPTOR.message_types_by_name['UserCreateObjectResponse'] = _USERCREATEOBJECTRESPONSE
DESCRIPTOR.message_types_by_name['PluginCreateDescriptionRequest'] = _PLUGINCREATEDESCRIPTIONREQUEST
DESCRIPTOR.message_types_by_name['PluginCreateDescriptionResponse'] = _PLUGINCREATEDESCRIPTIONRESPONSE
DESCRIPTOR.message_types_by_name['PluginTranslateDescriptionRequest'] = _PLUGINTRANSLATEDESCRIPTIONREQUEST
DESCRIPTOR.message_types_by_name['PluginTranslateDescriptionResponse'] = _PLUGINTRANSLATEDESCRIPTIONRESPONSE
DESCRIPTOR.message_types_by_name['PluginExtractExifDataRequest'] = _PLUGINEXTRACTEXIFDATAREQUEST
DESCRIPTOR.message_types_by_name['PluginExtractExifDataResponse'] = _PLUGINEXTRACTEXIFDATARESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Object = _reflection.GeneratedProtocolMessageType('Object', (_message.Message,), {
  'DESCRIPTOR' : _OBJECT,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:Object)
  })
_sym_db.RegisterMessage(Object)

Tag = _reflection.GeneratedProtocolMessageType('Tag', (_message.Message,), {
  'DESCRIPTOR' : _TAG,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:Tag)
  })
_sym_db.RegisterMessage(Tag)

UserCreateObjectRequest = _reflection.GeneratedProtocolMessageType('UserCreateObjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERCREATEOBJECTREQUEST,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:UserCreateObjectRequest)
  })
_sym_db.RegisterMessage(UserCreateObjectRequest)

UserCreateObjectResponse = _reflection.GeneratedProtocolMessageType('UserCreateObjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERCREATEOBJECTRESPONSE,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:UserCreateObjectResponse)
  })
_sym_db.RegisterMessage(UserCreateObjectResponse)

PluginCreateDescriptionRequest = _reflection.GeneratedProtocolMessageType('PluginCreateDescriptionRequest', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINCREATEDESCRIPTIONREQUEST,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:PluginCreateDescriptionRequest)
  })
_sym_db.RegisterMessage(PluginCreateDescriptionRequest)

PluginCreateDescriptionResponse = _reflection.GeneratedProtocolMessageType('PluginCreateDescriptionResponse', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINCREATEDESCRIPTIONRESPONSE,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:PluginCreateDescriptionResponse)
  })
_sym_db.RegisterMessage(PluginCreateDescriptionResponse)

PluginTranslateDescriptionRequest = _reflection.GeneratedProtocolMessageType('PluginTranslateDescriptionRequest', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINTRANSLATEDESCRIPTIONREQUEST,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:PluginTranslateDescriptionRequest)
  })
_sym_db.RegisterMessage(PluginTranslateDescriptionRequest)

PluginTranslateDescriptionResponse = _reflection.GeneratedProtocolMessageType('PluginTranslateDescriptionResponse', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINTRANSLATEDESCRIPTIONRESPONSE,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:PluginTranslateDescriptionResponse)
  })
_sym_db.RegisterMessage(PluginTranslateDescriptionResponse)

PluginExtractExifDataRequest = _reflection.GeneratedProtocolMessageType('PluginExtractExifDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINEXTRACTEXIFDATAREQUEST,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:PluginExtractExifDataRequest)
  })
_sym_db.RegisterMessage(PluginExtractExifDataRequest)

PluginExtractExifDataResponse = _reflection.GeneratedProtocolMessageType('PluginExtractExifDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINEXTRACTEXIFDATARESPONSE,
  '__module__' : 'mads_pb2'
  # @@protoc_insertion_point(class_scope:PluginExtractExifDataResponse)
  })
_sym_db.RegisterMessage(PluginExtractExifDataResponse)



_MADS_SERVICE = _descriptor.ServiceDescriptor(
  name='mads_service',
  full_name='mads_service',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=574,
  serialized_end=946,
  methods=[
  _descriptor.MethodDescriptor(
    name='userCreateObject',
    full_name='mads_service.userCreateObject',
    index=0,
    containing_service=None,
    input_type=_USERCREATEOBJECTREQUEST,
    output_type=_USERCREATEOBJECTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='pluginCreateDescription',
    full_name='mads_service.pluginCreateDescription',
    index=1,
    containing_service=None,
    input_type=_PLUGINCREATEDESCRIPTIONREQUEST,
    output_type=_PLUGINCREATEDESCRIPTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='pluginTranslateDescription',
    full_name='mads_service.pluginTranslateDescription',
    index=2,
    containing_service=None,
    input_type=_PLUGINTRANSLATEDESCRIPTIONREQUEST,
    output_type=_PLUGINTRANSLATEDESCRIPTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='pluginExtractExifData',
    full_name='mads_service.pluginExtractExifData',
    index=3,
    containing_service=None,
    input_type=_PLUGINEXTRACTEXIFDATAREQUEST,
    output_type=_PLUGINEXTRACTEXIFDATARESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MADS_SERVICE)

DESCRIPTOR.services_by_name['mads_service'] = _MADS_SERVICE

# @@protoc_insertion_point(module_scope)
