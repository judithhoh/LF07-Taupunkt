import time
from lcd_display import LcdDisplay
from scann_berechnen import TaupunktLogik
from taupunkt_db import taupunkt_db_class
from relay import relaypi

def main():
    datenbank = taupunkt_db_class()
    display = LcdDisplay()
    display.hintergundbeleuchtung_an()
    rechner = TaupunktLogik(4, 26)
    relay = relaypi(21)
    lufter = 0
    try:
        while True:
            rechner.daten_lesen()
            #print("V: "+str(rechner.berechnen()))
            rechner.berechnen()
            if rechner.delta_taupunkt > 0:
                lufter = 1
                relay.open()
            if rechner.delta_taupunkt <= 0:
                lufter = 0
                relay.close()
            #lüfter logig => if (rechner.berechnen == ? => dann lüfter an/aus
            datenbank.daten_schreiben(rechner.temperatur_innen, rechner.temperatur_aussen, rechner.humidity_innen,
                                      rechner.humidity_aussen, rechner.delta_taupunkt, lufter, rechner.taupunkt_innen,
                                      rechner.taupunkt_aussen)
            time.sleep(1)

    except KeyboardInterrupt:
        # LCD ausschalten.
        display.lcd.clear()
        display.hintergund_aus()
        datenbank.db.schliessen(datenbank.db)
        relay.cleanup()

if __name__ == '__main__':
    main()
