# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos import onnx_pb2 as onnx__pb2
from node_controller.gateway.protos import celaut_pb2 as celaut__pb2
from protos import solvers_dataset_pb2 as solvers__dataset__pb2
from grpcbigbuffer import buffer_pb2 as buffer__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tapi.proto\x12\x03\x61pi\x1a\nonnx.proto\x1a\x0c\x63\x65laut.proto\x1a\x15solvers_dataset.proto\x1a\x0c\x62uffer.proto\"L\n\x0eInterpretation\x12\x10\n\x08variable\x18\x01 \x03(\x05\x12\x18\n\x0bsatisfiable\x18\x02 \x01(\x08H\x00\x88\x01\x01\x42\x0e\n\x0c_satisfiable\"\x19\n\x06\x43lause\x12\x0f\n\x07literal\x18\x01 \x03(\x05\"\"\n\x03\x43nf\x12\x1b\n\x06\x63lause\x18\x01 \x03(\x0b\x32\x0b.api.Clause\"\x14\n\x04\x46ile\x12\x0c\n\x04\x66ile\x18\x01 \x01(\t\"\xa8\x03\n\x06Tensor\x12-\n\rspecification\x18\x01 \x01(\x0b\x32\x16.celaut.Service.Tensor\x12*\n\x07\x65scalar\x18\x02 \x01(\x0b\x32\x17.tensor_onnx.ModelProtoH\x00\x12\x36\n\x0bnon_escalar\x18\x03 \x01(\x0b\x32\x1f.api.Tensor.NonEscalarDimensionH\x00\x1a\x81\x02\n\x13NonEscalarDimension\x12?\n\x0bnon_escalar\x18\x01 \x03(\x0b\x32*.api.Tensor.NonEscalarDimension.NonEscalar\x1a\xa8\x01\n\nNonEscalar\x12-\n\x07\x65lement\x18\x01 \x01(\x0b\x32\x1c.dataset.SolverConfiguration\x12*\n\x07\x65scalar\x18\x02 \x01(\x0b\x32\x17.tensor_onnx.ModelProtoH\x00\x12\x36\n\x0bnon_escalar\x18\x03 \x01(\x0b\x32\x1f.api.Tensor.NonEscalarDimensionH\x00\x42\x07\n\x05modelB\x07\n\x05model2\xd6\x03\n\x06Solver\x12\x32\n\nStartTrain\x12\x0e.buffer.Buffer\x1a\x0e.buffer.Buffer\"\x00(\x01\x30\x01\x12\x31\n\tStopTrain\x12\x0e.buffer.Buffer\x1a\x0e.buffer.Buffer\"\x00(\x01\x30\x01\x12\x31\n\tGetTensor\x12\x0e.buffer.Buffer\x1a\x0e.buffer.Buffer\"\x00(\x01\x30\x01\x12\x34\n\x0cUploadSolver\x12\x0e.buffer.Buffer\x1a\x0e.buffer.Buffer\"\x00(\x01\x30\x01\x12\x32\n\nStreamLogs\x12\x0e.buffer.Buffer\x1a\x0e.buffer.Buffer\"\x00(\x01\x30\x01\x12-\n\x05Solve\x12\x0e.buffer.Buffer\x1a\x0e.buffer.Buffer\"\x00(\x01\x30\x01\x12\x31\n\tAddTensor\x12\x0e.buffer.Buffer\x1a\x0e.buffer.Buffer\"\x00(\x01\x30\x01\x12\x32\n\nGetDataSet\x12\x0e.buffer.Buffer\x1a\x0e.buffer.Buffer\"\x00(\x01\x30\x01\x12\x32\n\nAddDataSet\x12\x0e.buffer.Buffer\x1a\x0e.buffer.Buffer\"\x00(\x01\x30\x01\x32;\n\x06Random\x12\x31\n\tRandomCnf\x12\x0e.buffer.Buffer\x1a\x0e.buffer.Buffer\"\x00(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_INTERPRETATION']._serialized_start=81
  _globals['_INTERPRETATION']._serialized_end=157
  _globals['_CLAUSE']._serialized_start=159
  _globals['_CLAUSE']._serialized_end=184
  _globals['_CNF']._serialized_start=186
  _globals['_CNF']._serialized_end=220
  _globals['_FILE']._serialized_start=222
  _globals['_FILE']._serialized_end=242
  _globals['_TENSOR']._serialized_start=245
  _globals['_TENSOR']._serialized_end=669
  _globals['_TENSOR_NONESCALARDIMENSION']._serialized_start=403
  _globals['_TENSOR_NONESCALARDIMENSION']._serialized_end=660
  _globals['_TENSOR_NONESCALARDIMENSION_NONESCALAR']._serialized_start=492
  _globals['_TENSOR_NONESCALARDIMENSION_NONESCALAR']._serialized_end=660
  _globals['_SOLVER']._serialized_start=672
  _globals['_SOLVER']._serialized_end=1142
  _globals['_RANDOM']._serialized_start=1144
  _globals['_RANDOM']._serialized_end=1203
# @@protoc_insertion_point(module_scope)
