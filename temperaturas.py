import time
import schedule
from w1thermsensor import W1ThermSensor
from influxdb import InfluxDBClient


def insertar_temperatura():
	client = InfluxDBClient(host='localhost', port=8086)
	client.switch_database('temperaturas')

	sensor = W1ThermSensor()
	temperature = sensor.get_temperature()
	fecha = time.asctime()
	print("The temperature at: {} is {} celsius".format(fecha, temperature))

	json_body = [
		{
			"measurement": "tempEvents",
			"tags": {
				"user": "ja",
			},
			"time": fecha,
			"fields": {
				"temperatura": temperature
			}
		}
	]
	client.write_points(json_body)
	client.close()

#schedule.every().minute.do(insertar_temperatura)
schedule.every(1).hour.at("00:00").do(insertar_temperatura)
schedule.every(1).hour.at("00:30").do(insertar_temperatura)

while True:
	schedule.run_pending()
