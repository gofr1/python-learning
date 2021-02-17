In the current directory:

    protoc --python_out . weather.proto

weather_pb2.py would be generated.

Now open python3 or **ipython**:

    Python 3.8.3 (default, May 19 2020, 17:04:53) 
    Type 'copyright', 'credits' or 'license' for more information
    IPython 7.13.0 -- An enhanced Interactive Python. Type '?' for help.
    
    In [1]: import weather_pb2 as pb                                                                              
    
    In [2]: message = pb.Temperature(station = 's42', value = 24.2)                                               
    
    In [3]: message.time.GetCurrentTime()                                                                         
    
    In [4]: message                                                                                               
    Out[4]: 
    time {
      seconds: 1613584412
      nanos: 253623000
    }
    station: "s42"
    value: 24.2
    
    In [5]: data = message.SerializeToString()                                                                    
    
    In [6]: type(data)                                                                                            
    Out[6]: bytes
    
    In [7]: len(data)                                                                                             
    Out[7]: 27
    
    In [8]: message2 = pb.Temperature.FromString(data)                                                            
    
    In [9]: message2                                                                                              
    Out[9]: 
    time {
      seconds: 1613584412
      nanos: 253623000
    }
    station: "s42"
    value: 24.2
