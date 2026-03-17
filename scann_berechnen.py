import time
import RPi.GPIO as GPIO
import dht11
from taupunkt_berechnung import Taupunktberechung

class TaupunktLogik:

    def __init__(self, pin1, pin2):
        self.delta_taupunkt = None
        self.taupunkt_außen = None
        self.taupunkt_innen = None
        self.scanner_innen = dht11.DHT11(pin=pin1)
        self.scanner_außen = dht11.DHT11(pin=pin2)
        self.rechner = Taupunktberechung()
        self.temperatur_innen = 0.0
        self.temperatur_außen = 0.0
        self.humidity_innen = 0.0
        self.humidity_außen = 0.0

    def berechnen(self):
        self.taupunkt_innen = self.rechner.berechnen(self.temperatur_innen, self.humidity_innen)
        self.taupunkt_außen = self.rechner.berechnen(self.temperatur_außen, self.humidity_außen)
        self.delta_taupunkt = self.taupunkt_innen - self.taupunkt_außen
        return "Taupunkt-innen: "+self.taupunkt_innen +"\nTaupunkt-außen: "+self.taupunkt_außen + "\ndelta_Taupunkt: "+self.delta_taupunkt

    def daten_lesen(self):
        result=self.scanner_innen.lesen()
        self.temperatur_innen = result.temperature
        self.humidity_innen = result.humidity
        result=self.scanner_außen.lesen()
        self.temperatur_außen= result.temperature
        self.humidity_außen = result.humidity