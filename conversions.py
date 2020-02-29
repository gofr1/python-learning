# (°F - 32) x 5/9 = °C 

degree_value = int(input("Enter a temperature: "))
degree_type = ''

while degree_type not in ('C', 'F'):
    degree_type = input("Enter C for Celsius or F for Fahrenheit (C/F): ")

degree_out = 0

if degree_type == 'C':
    degree_out = (degree_value * 9.0 / 5.0) + 32
else:
    degree_out = (degree_value - 32) * 5.0 / 9.0

print(degree_out)

# The conversion formula for kph to mph is : 1 kilometre = 0.621371192 miles

speed_value = int(input("Enter a speed value: "))
speed_type = ''

while speed_type not in ('K', 'M'):
    speed_type = input("Enter K for kph or M for mph (K/M): ")

speed_out = 0
speed_rate = 0.621371192

if speed_type == 'K':
    speed_out = speed_value * speed_rate
else:
    speed_out = speed_value / speed_rate

print(speed_out)