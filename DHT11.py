import time
import RPi.GPIO as GPIO
import dht11
import LcdDisplay


class dht11:
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
    sensor = dht11()
    display = LcdDisplay.LcdDisplay()
    try:
        while True:
            display.nachricht(sensor.lesen())
            time.sleep(1)

    except KeyboardInterrupt:
        # LCD ausschalten.
        display.lcd.clear()
        display.hintergund_aus()

if __name__ == '__main__':
    main()