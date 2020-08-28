

# This file is executed on every boot (including wake-boot from deepsleep)

#import esp

#esp.osdebug(None)
import webrepl

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

webrepl.start()

