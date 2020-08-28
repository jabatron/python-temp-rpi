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
import json

import onewire, ds18x20
import binascii

import esp
esp.osdebug(None)
import dht
import gc
gc.collect()

ssid = 'jabatronic__'
password = 'clavel08'
mqtt_server = '192.168.8.88'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'temp/salon/sync'
topic_pub = b'temp/salon'

last_message = 0
message_interval = 5
counter = 0
d = {}
ubicacion = 'Salon'
print ("Hola")

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while station.isconnected() == False:
  pass
print ("Wifi Conectada")
sleep (2)

ledpin = Pin(14, Pin.OUT)

while True:
  ledpin.value(1)
  print ('Enciendo LED')
  sleep(1)
  ledpin.value(0)
  print('Apago LED')
  sleep(1)

