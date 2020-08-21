import dht
from machine import Pin
from time import sleep

pindht = Pin(14)
ledpin = Pin(2, Pin.OUT)
sensor = dht.DHT22(pindht)

while True:
  try:
    ledpin.value(1)
    sensor.measure()
    slee(1)
    ledpin.value(0)
    temp = sensor.temperature()
    hum = sensor.humidity()
    print (temp)
    if (isinstance(temp, float) and isinstance(hum, float)) or (isinstance(temp, int) and isinstance(hum, int)):
      msg = (b'{0:3.1f},{1:3.1f}'.format(temp, hum))

      # uncomment for Fahrenheit
      #temp = temp * (9/5) + 32.0

      hum = round(hum, 2)
      print(msg)
    else:
      print('Invalid sensor readings.')
  except OSError as e:
    print ('Failed to read sensor.')
    
  sleep(1)
