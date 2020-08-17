import time
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()
temperature = sensor.get_temperature()
fecha = time.asctime()
print("The temperature at: {} is {} celsius".format(fecha, temperature))
print("Identificador del sensor: {}".format(sensor.id))

print("Hola")
