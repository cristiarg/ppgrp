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
        request_serializer=proxy__pb2.ServiceSessionRequest.SerializeToString,
        response_deserializer=proxy__pb2.ServiceSessionResponse.FromString,
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


def add_SessionDispatcherServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Request': grpc.unary_unary_rpc_method_handler(
          servicer.Request,
          request_deserializer=proxy__pb2.ServiceSessionRequest.FromString,
          response_serializer=proxy__pb2.ServiceSessionResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ppgrp.SessionDispatcher', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))