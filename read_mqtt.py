import paho.mqtt.client as mqtt #import the client1
import time

broker_address="192.168.8.88" 

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
#client.publish("house/main-light","OFF")#publish
client.subscribe('hello',qos=2)

time.sleep(4) # wait
client.loop_stop() #stop the loop