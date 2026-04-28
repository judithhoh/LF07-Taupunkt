import time
import RPi.GPIO as GPIO
import dht11

class Dht11Sensor:
    def __init__(self, pin):
        # initialisiere GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()
        # lesen der Daten ueber Pin 4
        self.scanner = dht11.DHT11(pin=pin)

    def lesen(self):
        result = self.scanner.read()
        count = 0
        while not result.is_valid():  # lesen bis Werte ok sind
            if count%20==0:
                print("messung...")
            if count == 100:
                return "Messung war nicht möglich"
            result = self.scanner.read()
            count=count+1
        return result

    def lesen_display(self):
        result = self.scanner.read()
        count = 0
        while not result.is_valid():  # lesen bis Werte ok sind
            if count%20==0:
                print("messung...")
            if count == 100:
                return "Messung war nicht möglich"
            result = self.scanner.read()
            count=count+1
        return "Temperature: %-3.1f C" % result.temperature + "\nHumidity: %-3.1f %%" % result.humidity


def main():
    sensor = Dht11Sensor(4)
    try:
        while True:
            print(sensor.lesen())
            time.sleep(1)

    except KeyboardInterrupt:
        # LCD ausschalten.
        print("Ende")

if __name__ == '__main__':
    main()