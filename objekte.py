from relay import relaypi
from scann_berechnen import TaupunktLogik

print("ERSTELLE RECHNER")

rechner = TaupunktLogik(4, 26)

print("RECHNER FERTIG")
print("ERSTELLE RELAY")

relay = relaypi(21)

print("RELAY FERTIG")

