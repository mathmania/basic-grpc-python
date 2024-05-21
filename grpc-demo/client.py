from __future__ import print_function

import logging

import grpc
import schema_pb2
import schema_pb2_grpc

VALUE_1 = 86
VALUE_2 = 42

def run():
    print("Will try to Add() {v1} and {v2}".format(v1=VALUE_1, v2=VALUE_2))
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = schema_pb2_grpc.ArithmeticStub(channel)
        response = stub.Add(schema_pb2.AddRequest(value_1=VALUE_1, value_2=VALUE_2))
    print("Add() response {r}".format(r=response.response))


if __name__ == "__main__":
    logging.basicConfig()
    run()