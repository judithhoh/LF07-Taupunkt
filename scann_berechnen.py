from dht11_jh import Dht11Sensor as dht11
from taupunkt_berechnung import Taupunktberechnung

class TaupunktLogik:

    def __init__(self, pin1, pin2):
        self.delta_taupunkt = None
        self.taupunkt_aussen = None
        self.taupunkt_innen = None
        self.scanner_innen = dht11(pin=pin1)
        self.scanner_aussen = dht11(pin=pin2)
        self.rechner = Taupunktberechnung()
        self.temperatur_innen = 0.0
        self.temperatur_außen = 0.0
        self.humidity_innen = 0.0
        self.humidity_außen = 0.0

    def berechnen(self):
        self.taupunkt_innen = self.rechner.berechnen(self.temperatur_innen, self.humidity_innen)
        self.taupunkt_aussen = self.rechner.berechnen(self.temperatur_außen, self.humidity_außen)
        self.delta_taupunkt = self.taupunkt_innen - self.taupunkt_aussen
        return "Taupunkt-innen: "+str(self.taupunkt_innen) +"\nTaupunkt-außen: "+str(self.taupunkt_aussen) + "\ndelta_Taupunkt: "+str(self.delta_taupunkt)

    def daten_lesen(self):
        result=self.scanner_innen.lesen()
        self.temperatur_innen = result.temperature
        print("temperatur_innen"+str(self.temperatur_innen))
        self.humidity_innen = result.humidity
        print("humidity_innen" + str(self.humidity_innen))
        result=self.scanner_aussen.lesen()
        self.temperatur_außen= result.temperature
        print("temperatur_außen" + str(self.temperatur_außen))
        self.humidity_aussen = result.humidity
        print("humidity_außen" + str(self.humidity_außen))