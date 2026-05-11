import time
#from lcd_display import LcdDisplay
from objekte import relay, rechner

from taupunkt_db import taupunkt_db_class

def main():
    #display = LcdDisplay()
    #display.hintergundbeleuchtung_an()
    datenbank = taupunkt_db_class()

    relay.close()
    lufter = 0
    try:
        while True:
            rechner.daten_lesen()
            #print("V: "+str(rechner.berechnen()))
            rechner.berechnen()
            print("delta: "+str(rechner.delta_taupunkt))
            if rechner.delta_taupunkt > 0:
                lufter = 1
                relay.open()
                print("lüfter an")
            if rechner.delta_taupunkt <= 0:
                lufter = 0
                relay.close()
                print("lüfter aus")
            datenbank.daten_schreiben(rechner.temperatur_innen, rechner.temperatur_aussen, rechner.humidity_innen,
                                      rechner.humidity_aussen, rechner.delta_taupunkt, lufter, rechner.taupunkt_innen,
                                      rechner.taupunkt_aussen)
            time.sleep(1)

    except KeyboardInterrupt:
        # LCD ausschalten.
        #display.lcd.clear()
        #display.hintergund_aus()
        datenbank.db.schliessen(datenbank.db)
        relay.cleanup()

if __name__ == '__main__':
    main()