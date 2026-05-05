import time
from dht11_jh import Dht11Sensor
from lcd_display import LcdDisplay
from scann_berechnen import TaupunktLogik
from taupunkt_db import taupunkt_db_class

def main():
    datenbank = taupunkt_db_class()
    display = LcdDisplay()
    display.hintergundbeleuchtung_an()
    rechner = TaupunktLogik(4, 26)
    try:
        while True:
            #print("Sensor1:"+sensor.lesen_display())
            #print("Sensor2:"+sensor2.lesen_display())
            rechner.daten_lesen()
            #print("V: "+str(rechner.berechnen()))
            rechner.berechnen()
            lufter = 0
            #lüfter logig => if (rechner.berechnen == ? => dann lüfter an/aus (extra Klasse für Lüfter)
            datenbank.daten_schreiben(rechner.temperatur_innen, rechner.temperatur_aussen, rechner.humidity_innen,
                                      rechner.humidity_aussen, rechner.delta_taupunkt, lufter, rechner.taupunkt_innen,
                                      rechner.taupunkt_aussen)
            time.sleep(1)

    except KeyboardInterrupt:
        # LCD ausschalten.
        display.lcd.clear()
        display.hintergund_aus()
        datenbank.db.schliessen(datenbank.db)

if __name__ == '__main__':
    main()
