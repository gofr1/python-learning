# To install gRPC

    pip install grpcio-tools

# To use it:

    python3 -m grpc_tools.protoc -I. --python_out . --grpc_python_out . weather.proto

`-I.` - look in current directory  
`--python_out . ` emmit files into current directory  
`--grpc_python_out . ` emmit grpc definitions into current folder  
`weather.proto` definition file