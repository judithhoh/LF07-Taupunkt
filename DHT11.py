import time
import RPi.GPIO as GPIO
import dht11
import LcdDisplay

# initialisiere GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
# lesen der Daten ueber Pin 4
instance = dht11.DHT11(pin = 4)
result = instance.read()
while not result.is_valid(): # lesen bis Werte ok sind
    result = instance.read()

display = LcdDisplay.LcdDisplay
nachricht = "Temperature: %-3.1f C" % result.temperature
display.nachricht(nachricht)
time.sleep(1)
nachricht = "Humidity: %-3.1f %%" % result.humidity
display.nachricht(nachricht)
