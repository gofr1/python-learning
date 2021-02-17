import grpc

import weather_pb2 as pb
import weather_pb2_grpc as gpb

# Create message
message = pb.Temperature(station = 'NYC', value = 3.6)
message.time.GetCurrentTime()
print('sending:', message)


with grpc.insecure_channel('localhost:9999') as chan:
    stub = gpb.WeatherStub(chan)
    resp = stub.AddTemperature(message)
    print(f'total of {resp.record_count} records')