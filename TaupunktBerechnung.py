import math

def taupunkt(temperatur, humidity):
    a = 0.0
    b = 0.0
    #parameter setzten
    if temperatur >= 0:
        a = 7.5
        b = 237.3
    else:
        a = 7.6
        b = 240.7
    c = 6.1078
    # Sättigungsdampfdruck in hPa
    saettigungsdampfdruck = c * pow(10, (a * temperatur)/(b+temperatur))

    # Dampfdruck in hPa
    dampfdruk = saettigungsdampfdruck * (humidity / 100)

    #v-Parameter
    v = math.log10(dampfdruk / c)

    # Taupunkttemperatur (°C)
    tt = (b * v) / (a-v);
    return {tt}