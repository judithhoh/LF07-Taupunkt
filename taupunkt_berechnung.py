import math


class Taupunktberechnung:


    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.temperatur = 0.0
        self.humidity = 0.0
        self.c = 6.1078
    def berechnen(self, temperatur, humidity):
        self.temperatur = temperatur
        print("Temperatur "+str(self.temperatur))
        self.humidity = humidity
        #parameter setzten
        self.parameter_setzen()
        # Sättigungsdampfdruck in hPa
        sd = self.saettingugnsdampfdruck()
        #print("Seattingungsdampfdruck "+str(sd))
        # Dampfdruck in hPa
        dd = self.dampfdruck(sd)
        #print("Dampfdruck " + str(dd))
        print()
        #v-Parameter
        v = self.v_parameter(dd)
        #print("V"+str(v))
        # Taupunkttemperatur (°C)
        return self.taupunkttemperatur(v)

    def parameter_setzen(self):
        if self.temperatur >= 0:
            self.a = 7.5
            self.b = 237.3
        else:
            self.a = 7.6
            self.b = 240.7

    def saettingugnsdampfdruck(self):
        return self.c * pow(10, (self.a * self.temperatur) / (self.b + self.temperatur))

    def dampfdruck(self, saettingungsdampfdruck):
        return saettingungsdampfdruck * (self.humidity / 100)

    def v_parameter(self, dampfdruck):
        return math.log10(dampfdruck / self.c)

    def taupunkttemperatur(self, v):
        return (self.b * v) / (self.a - v)
