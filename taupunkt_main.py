import time
from dht11_jh import Dht11Sensor
from lcd_display import LcdDisplay
from scann_berechnen import TaupunktLogik

def main():
    sensor = Dht11Sensor(4)
    sensor2 = Dht11Sensor(26)
    display = LcdDisplay()
    display.hintergundbeleuchtung_an()
    #rechner = TaupunktLogik(4, 37)
    rechner = TaupunktLogik(4, 26)
    try:
        while True:
            rechner.daten_lesen()
            rechner.daten_lesen()
            rechner.berechnen()
            time.sleep(1)

    except KeyboardInterrupt:
        # LCD ausschalten.
        display.lcd.clear()
        display.hintergund_aus()

if __name__ == '__main__':
    main()
