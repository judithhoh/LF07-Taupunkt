#!/usr/bin/python

import RPi.GPIO as GPIO
import time

class relaypi:
    def __init__(self, pin):
        self.relay_pin = pin
        # Board Modus GPIO.BOARD
        GPIO.setmode(GPIO.BOARD)
        # relay_pin als Ausgang
        GPIO.setup(self.relay_pin, GPIO.OUT)
    def open(self):
        GPIO.output(self.relay_pin, GPIO.LOW)
    def close(self):
        # schliesse Relais
        GPIO.output(self.relay_pin, GPIO.HIGH)
    def cleanup(self):
        GPIO.cleanup()

def main():
   test = relay(40)
   # Oeffne Relais
   test.open()
   # warte eine halbe Sekunde
   time.sleep(0.5)
   # schliesse Relais
   test.close()
   test.cleanup()

if __name__ == '__main__':
    main()





