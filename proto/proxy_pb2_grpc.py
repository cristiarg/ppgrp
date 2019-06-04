# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import proxy_pb2 as proxy__pb2


class SessionDispatcherStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Request = channel.unary_unary(
        '/ppgrp.SessionDispatcher/Request',
        request_serializer=proxy__pb2.RequestSessionRequest.SerializeToString,
        response_deserializer=proxy__pb2.RequestSessionResponse.FromString,
        )
    self.Release = channel.unary_unary(
        '/ppgrp.SessionDispatcher/Release',
        request_serializer=proxy__pb2.ReleaseSessionRequest.SerializeToString,
        response_deserializer=proxy__pb2.ReleaseSessionResponse.FromString,
        )


class SessionDispatcherServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Request(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Release(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SessionDispatcherServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Request': grpc.unary_unary_rpc_method_handler(
          servicer.Request,
          request_deserializer=proxy__pb2.RequestSessionRequest.FromString,
          response_serializer=proxy__pb2.RequestSessionResponse.SerializeToString,
      ),
      'Release': grpc.unary_unary_rpc_method_handler(
          servicer.Release,
          request_deserializer=proxy__pb2.ReleaseSessionRequest.FromString,
          response_serializer=proxy__pb2.ReleaseSessionResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ppgrp.SessionDispatcher', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
