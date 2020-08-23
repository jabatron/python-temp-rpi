import time
import json
import paho.mqtt.client as mqtt # import the client1

broker_address = "192.168.8.88"
broker_port = 1883
topic = "temp/salon"

def on_message(client, userdata, message):
    msg = message.payload.decode("utf-8")
    print("Mensaje recibido=", str(message.payload.decode("utf-8")))
    print (msg)
    print (type(msg))
    d = json.loads(msg)
    print (d)
    print (type(d))
    #print("Topic=", message.topic)
    #print("Nivel de calidad [0|1|2]=", message.qos)
    #print("Flag de retención o nuevo?=", message.retain)

client = mqtt.Client("Subscriptor_ejem1")
client.on_message = on_message 
client.connect(broker_address) 
client.loop_start() # Inicio del bucle
client.subscribe(topic)
while True: # Paramos el hilo para recibir mensajes.
    pass
client.loop_stop() # Fin del bucle