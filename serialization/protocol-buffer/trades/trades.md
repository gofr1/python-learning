    Python 3.8.3 (default, May 19 2020, 17:04:53) 
    Type 'copyright', 'credits' or 'license' for more information
    IPython 7.13.0 -- An enhanced Interactive Python. Type '?' for help.
    
    In [1]: import trades_pb2 as tpb                                                                              
    
    In [2]: import trades as tr                                                                                   
    
    In [3]: tr.trades[0]                                                                                          
    Out[3]: 
    {'time': datetime.datetime(2020, 5, 1, 13, 23, 32),
     'symbol': 'AAPL',
     'volume': 100,
     'price': 310.13,
     'buy': True}
     
    In [4]: m = tr.trades[0]
    
    In [5]: message = tpb.Trades(symbol = m['symbol'], volume=  m['volume'],price = m['price'], buy = m['buy'])  
    
    In [6]: message.time.FromDatetime(m['time'])                                                                 
    
    In [7]: message                                                                                              
    Out[7]: 
    time {
      seconds: 1588339412
    }
    symbol: "AAPL"
    volume: 100
    price: 310.13
    buy: true
        
    In [8]: data_len = 0                                                                                          
    
    In [9]: for trade in tr.trades: 
       ...:     message = tpb.Trades(symbol = trade['symbol'], volume= trade['volume'],price = trade['price'], buy
       ...:  = trade['buy']) 
       ...:     message.time.FromDatetime(trade['time']) 
       ...:     data = message.SerializeToString() 
       ...:     data_len+= len(data) 
       ...:                                                                                                       
    
    In [10]: print(f'total data size is {data_len}')                                                               
    total data size is 52
