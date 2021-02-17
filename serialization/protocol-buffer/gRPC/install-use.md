# To install gRPC

    pip install grpcio-tools

# To use it:

    python3 -m grpc_tools.protoc -I. --python_out . --grpc_python_out . weather.proto

`-I.` - look in current directory  
`--python_out . ` emmit files into current directory  
`--grpc_python_out . ` emmit grpc definitions into current folder  
`weather.proto` definition file

Now in terminal#1 launch

    python3 server.py
    2021-02-17 21:20:53,903 - INFO - server ready on 9999

In terminal#2 launch

    python3 client.py
    sending: time {
      seconds: 1613586485
      nanos: 351678000
    }
    station: "NYC"
    value: 3.6
    
    total of 1 records

And on terminal#1 you will see:

    2021-02-17 21:28:05,358 - INFO - add: time {
      seconds: 1613586485
      nanos: 351678000
    }
    station: "NYC"
    value: 3.6
