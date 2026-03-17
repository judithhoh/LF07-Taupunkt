import time
from dht11_jh import Dht11Sensor
from lcd_display import LcdDisplay
from scann_berechnen import TaupunktLogik

def main():
    sensor = Dht11Sensor()
    display = LcdDisplay()
    display.hintergundbeleuchtung_an()
    #rechner = TaupunktLogik(4, )
    try:
        while True:
            #rechner.berechnen()
            print(sensor.lesen_display())
            time.sleep(1)

    except KeyboardInterrupt:
        # LCD ausschalten.
        display.lcd.clear()
        display.hintergund_aus()

if __name__ == '__main__':
    main()
