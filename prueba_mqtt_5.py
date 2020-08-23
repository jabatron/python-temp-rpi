
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

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

pindht = Pin(14)
ledpin = Pin(2, Pin.OUT)
sensor = dht.DHT22(machine.Pin(14))

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

p = 0
def sub_cb(topic, msg):
  print((topic, msg))
  client.publish(topic_pub, b'received')
  if str(msg) == "b'ja'":
    print ('ja es el mejor')
      
  
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

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    new_message = client.check_msg()
    
    #time.sleep(1)
  except OSError as e:
    restart_and_reconnect()




