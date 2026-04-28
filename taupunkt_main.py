import time
from dht11_jh import Dht11Sensor
from lcd_display import LcdDisplay
from scann_berechnen import TaupunktLogik
from datenbank import sqlite_datenbank

def main():
    datenbank = sqlite_datenbank()
    datenbank.verbinden()
    datenbank.tabelle_erstellen()
    datenbank.daten_einfuegen()
    datenbank.abfrage()
    datenbank.schliessen()
    sensor = Dht11Sensor(4)
    sensor2 = Dht11Sensor(26)
    display = LcdDisplay()
    display.hintergundbeleuchtung_an()
    rechner = TaupunktLogik(4, 26)
    try:
        while True:
            #print("Sensor1:"+sensor.lesen_display())
            #print("Sensor2:"+sensor2.lesen_display())
            rechner.daten_lesen()
            print("V: "+str(rechner.berechnen()))
            time.sleep(1)

    except KeyboardInterrupt:
        # LCD ausschalten.
        display.lcd.clear()
        display.hintergund_aus()

if __name__ == '__main__':
    main()
