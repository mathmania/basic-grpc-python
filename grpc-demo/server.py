from concurrent import futures
import logging

import grpc
import schema_pb2
import schema_pb2_grpc


class AddService(schema_pb2_grpc.ArithmeticServicer):
    def Add(self, request, context):
        computedValue = request.value_1 + request.value_2
        return schema_pb2.AddReply(response=computedValue)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    schema_pb2_grpc.add_ArithmeticServicer_to_server(AddService(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()