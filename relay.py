#!/usr/bin/python

import RPi.GPIO as GPIO
import time

class relaypi:
    def __init__(self, pin):
        self.relay_pin = pin
        self.state = False
        # Board Modus GPIO.BOARD
        GPIO.setmode(GPIO.BCM)
        # relay_pin als Ausgang
        GPIO.setup(self.relay_pin, GPIO.OUT)
    def open(self):
        GPIO.output(self.relay_pin, GPIO.LOW)
        self.state = True
    def close(self):
        # schliesse Relais
        GPIO.output(self.relay_pin, GPIO.HIGH)
        self.state = False
    def get_state(self):
            return self.state
    def cleanup(self):
        GPIO.cleanup()

def main():
   test = relaypi(40)
   # Oeffne Relais
   test.open()
   # warte eine halbe Sekunde
   time.sleep(0.5)
   # schliesse Relais
   test.close()
   test.cleanup()

if __name__ == '__main__':
    main()





