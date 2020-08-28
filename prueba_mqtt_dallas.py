

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

ledpin = Pin(1, Pin.OUT)
print (ledpin)
ds_pin = machine.Pin(14)
print (ds_pin)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))


roms = ds_sensor.scan()

bsensorID = (binascii.hexlify(roms[0]))
sensorID = bsensorID.decode("utf-8")
print('Found DS devices: {} en hex: {}'.format(roms, sensorID))


print('Connection successful')
print(station.ifconfig())


def sub_cb(topic, msg):
  print((topic, msg))
  #print ("El mesaje es: {}".format(msg))
  if topic == b'temp/salon/sync' and msg == b'leer_temp':
    print('Mensaje para leer la temperatura')
  
    try:
      d = leer_temp()
      msgc=json.dumps(d)
      print ("Valor de d: {}".format(d))
      client.publish(topic_pub, msgc)
    except OSError as e:
      restart_and_reconnect()
    
def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()
  
  
def leer_temp():
  ledpin.value(1)
  print ('Enciendo LED')
  
  th = {}
  ds_sensor.convert_temp()
  time.sleep_ms(750)
  temp = ds_sensor.read_temp(roms[0])
  th['temp']=temp
  th['sensorID']=sensorID
  th['site']=ubicacion
  print(th)
  ledpin.value(0)
  print('Apago LED')

  return th
  
  
try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()
  
d = leer_temp()

print ("Primer valor de d= {}".format(d))
  
 
while True:
  try:
    new_message = client.check_msg()
    
    #time.sleep(1)
  except OSError as e:
    restart_and_reconnect()







