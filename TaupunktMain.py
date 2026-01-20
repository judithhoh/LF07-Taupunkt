import time
import DHT11
import LcdDisplay

def main():
    sensor = DHT11.dht11Sensor()
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
