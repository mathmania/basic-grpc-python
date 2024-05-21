# GRPC Demo

This is a simple demo of how to use gRPC in Python.

The code is generated with : 
```bash
poetry run python -m grpc_tools.protoc -I ./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/schema.proto
```

- **schema_pb2.py** Contains the generated classes service defined in the schema.proto file.
- **schema_pb2_grpc.py** Contains the generated classes for the client defined in the schema.proto file.


## Running the server
```bash
poetry run python server.py
```

## Running the client
```bash
poetry run python client.py
```


## Docs
- **Poetry**: https://python-poetry.org/docs/configuration/
- **gRPC**: https://grpc.io/docs/languages/python/basics/
- **mise**: https://mise.jdx.dev/
