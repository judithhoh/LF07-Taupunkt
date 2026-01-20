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
display = LcdDisplay.LcdDisplay()
try:
    while True:
        result = instance.read()
        while not result.is_valid(): # lesen bis Werte ok sind
            result = instance.read()
        nachricht = "Temperature: %-3.1f C" % result.temperature +"\nHumidity: %-3.1f %%" % result.humidity
        display.nachricht(nachricht)
        time.sleep(1)

except KeyboardInterrupt:
    # LCD ausschalten.
    display.hintergund_aus()