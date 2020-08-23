import time
import schedule
import paho.mqtt.client as paho
from influxdb import InfluxDBClient

broker="192.168.8.88"
port=1883

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    print(client)
    pass

def pedir_temperatura():
	client1= paho.Client("rpi-zero")                           #create client object
	client1.on_publish = on_publish                              #assign function to callback
	client1.connect(broker,port)                                 #establish connection
	ret= client1.publish("temp/salon/sync","leer_temp")          #publish

def insertar_temperatura():
	client = InfluxDBClient(host='localhost', port=8086)
	client.switch_database('temperaturas')

	fecha = time.asctime()
	pedir_temperatura()
	temperature = 28
	sensorID='aabbcc' 
	print("The temperature at: {} is {} celsius".format(fecha, temperature))

	json_body = [
		{
			"measurement": "tempEvents",
			"tags": {
				"user": "ja",
#				"sensorID": "28-" + sensor.id,
				"site": "home-sitting room"
			},
			"time": fecha,
			"fields": {
				"temperatura": temperature
			}
		}
	]
	#client.write_points(json_body)
	client.close()

#schedule.every().minute.do(insertar_temperatura)
#schedule.every(1).hour.at("00:00").do(insertar_temperatura)
#schedule.every(1).hour.at("00:30").do(insertar_temperatura)
insertar_temperatura()

#while True:
#	schedule.run_pending()
