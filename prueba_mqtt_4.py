
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
d = {}

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


def sub_cb(topic, msg):
  print((topic, msg))
  #print ("El mesaje es: {}".format(msg))
  if topic == b'temp/salon/sync' and msg == b'leer_temp_hum':
    print('Mensaje para leer la temperatura')
  
    try:
      d = leer_temp_hum()
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
  
  
def leer_temp_hum():
  ledpin.value(1)
  print ('Enciendo LED')
  
  th = {}
  try:
    sensor.measure()
    #time.sleep(1)
    temp = sensor.temperature()
    hum = sensor.humidity()
    if (isinstance(temp, float) and isinstance(hum, float)) or (isinstance(temp, int) and isinstance(hum, int)):
      #d = {'temp': 0, 'humidity': 0}
      
      th['temp']=temp
      th['humidity']=hum
      # uncomment for Fahrenheit
      #temp = temp * (9/5) + 32.0

      hum = round(hum, 2)
      #print(th)
      
    else:
      print('Invalid sensor readings.')
  except OSError as e:
    print ('Failed to read sensor.')
  
  ledpin.value(0)
  print('Apago LED')

  return th
  
  
try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()
  
d = leer_temp_hum()
print ("Primer valor de d= {}".format(d))
  
 
while True:
  try:
    new_message = client.check_msg()
    
    #time.sleep(1)
  except OSError as e:
    restart_and_reconnect()




