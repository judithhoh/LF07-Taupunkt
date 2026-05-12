from relay import relaypi

print("ERSTELLE RELAY")

relay = relaypi(21)

print("RELAY FERTIG")

from scann_berechnen import TaupunktLogik

print("ERSTELLE RECHNER")

rechner = TaupunktLogik(4, 26)

print("RECHNER FERTIG")