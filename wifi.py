
try:
  import usocket as socket
except:
  import socket
import time
from machine import Pin
from time import sleep
from umqttsimple import MQTTClient
import ubinascii
import machine
from machine import Pin
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

ssid = 'jabatronic__'
password = 'clavel08'

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())



