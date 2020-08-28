import machine
from machine import Pin
from time import sleep

print ('Uno')
ledpin = Pin(14, Pin.OUT)
print ('dos')

while True:
  ledpin.value(1)
  print ('Enciendo LED')
  sleep(1)
  ledpin.value(0)
  print('Apago LED')
  sleep(1)

