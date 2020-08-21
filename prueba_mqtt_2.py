
try:
  import usocket as socket
except:
  import socket
import time
from umqttsimple import MQTTClient
import ubinascii
import machine
from machine import Pin
import micropython
import network
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
topic_sub = b'notification'
topic_pub = b'hello'

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


def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'notification' and msg == b'received':
    print('ESP received hello message')

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
    ledpin.value(1)
    print ('Enciendo LED')
    sensor.measure()
    sleep(1)
    ledpin.value(0)
    print('Apago LED')
    sleep(1)
    temp = sensor.temperature()
    hum = sensor.humidity()
    if (isinstance(temp, float) and isinstance(hum, float)) or (isinstance(temp, int) and isinstance(hum, int)):
      msg = ("{0:3.2f}C - {1:3.2f}%h".format(temp, hum))
      msg2 = [temp, hum]
      msg3 = str (msg2) + str(counter)
      print (msg3)
      # uncomment for Fahrenheit
      #temp = temp * (9/5) + 32.0

      hum = round(hum, 2)
      #print(msg)
      
      try:
        #client.check_msg()
        if (time.time() - last_message) > message_interval:
          #msg = b'Hello #%d' % counter
          print (msg)
          client.publish(topic_pub, msg3)
          client.publish(topic_pub, msg3)
          client.publish(topic_pub, msg3)
          last_message = time.time()
          counter += 1
      except OSError as e:
        restart_and_reconnect()
      
      
      
    else:
      print('Invalid sensor readings.')
  except OSError as e:
    print ('Failed to read sensor.')
    
  sleep(5)  

