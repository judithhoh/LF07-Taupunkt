import threading
import time

from app import app
from taupunkt_scanner import main
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

if __name__ == '__main__':
    t = threading.Thread(target=main)
    t.daemon = True
    t.start()
    time.sleep(1)
    app.run(host="0.0.0.0", port=5000, debug=True) # vorord nochmal testen
