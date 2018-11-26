# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import faces.facematrix_pb2 as facematrix__pb2


class FaceTransformStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.getMatrix = channel.unary_unary(
            '/facematrix.FaceTransform/getMatrix',
            request_serializer=facematrix__pb2.Face.SerializeToString,
            response_deserializer=facematrix__pb2.Matrix.FromString,
        )


class FaceTransformServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def getMatrix(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FaceTransformServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'getMatrix': grpc.unary_unary_rpc_method_handler(
            servicer.getMatrix,
            request_deserializer=facematrix__pb2.Face.FromString,
            response_serializer=facematrix__pb2.Matrix.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'facematrix.FaceTransform', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
