import time
from dht11_jh import Dht11Sensor
from lcd_display import LcdDisplay
from scann_berechnen import TaupunktLogik

def main():
    sensor = Dht11Sensor(4)
   # sensor2 = Dht11Sensor(37)
    display = LcdDisplay()
    display.hintergundbeleuchtung_an()
    #rechner = TaupunktLogik(4, 37)
    try:
        while True:
            #rechner.berechnen()
            print("Sensor1:"+sensor.lesen_display())
            #print("Sensor2:"+sensor2.lesen_display())
            time.sleep(1)

    except KeyboardInterrupt:
        # LCD ausschalten.
        display.lcd.clear()
        display.hintergund_aus()

if __name__ == '__main__':
    main()
