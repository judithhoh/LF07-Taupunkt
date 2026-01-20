import time
import RPi.GPIO as GPIO
import dht11

class dht11Sensor:
    def __init__(self):
        # initialisiere GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()
        # lesen der Daten ueber Pin 4
        self.instance = dht11.DHT11(pin=4)
    def lesen(self):
        result = self.instance.read()
        while not result.is_valid():  # lesen bis Werte ok sind
            result = self.instance.read()
        return "Temperature: %-3.1f C" % result.temperature + "\nHumidity: %-3.1f %%" % result.humidity


def main():
    sensor = dht11Sensor()
    try:
        while True:
            print(sensor.lesen())
            time.sleep(1)

    except KeyboardInterrupt:
        # LCD ausschalten.
        print("Ende")

if __name__ == '__main__':
    main()