#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import board
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd

class LcdDisplay:
    def __init__(self):
        # Definiere LCD Zeilen und Spaltenanzahl.
        lcd_columns = 16
        lcd_rows = 2
        # Initialisierung I2C Bus
        i2c = busio.I2C(board.SCL, board.SDA)
        # Festlegen des LCDs in die Variable LCD
        self.lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows)

    def hintergundbeleuchtung_an(self):
        self.lcd.backlight = True

    def nachricht(self, nachricht):
        self.lcd.clear()
        self.lcd.message = nachricht

    def curser(self):
        self.lcd.clear()
        self.lcd.cursor = True
        self.lcd.message = "Show Cursor!"

    def curser_blinken(self):
        self.lcd.clear()
        self.lcd.blink = True
        self.lcd.message = "Blinky Cursor!"

    def curser_aus(self):
        self.lcd.blink = False
        self.lcd.clear()

    def nachricht_scroll(self, nachricht):
        self.lcd.clear()
        scroll_msg = nachricht
        for i in range(len(scroll_msg)):
            time.sleep(0.5)
            self.lcd.move_right()
        for i in range(len(scroll_msg)):
            time.sleep(0.5)
            self.lcd.move_left()

    def hintergrund_blinken(self):
        self.lcd.backlight = False
        time.sleep(1.0)
        self.lcd.backlight = True
        time.sleep(1.0)
        self.lcd.backlight = False

    def hintergund_aus(self):
        self.lcd.clear()
        self.lcd.backlight = False

def main():
    display = LcdDisplay()
    try:
        # Hintergrundbeleuchtung einschalten
        display.hintergundbeleuchtung_an()
        # Zwei Worte mit Zeilenumbruch werden ausgegeben
        display.nachricht("Hallo\nWelt!")
        # 5 Sekunden warten
        time.sleep(5.0)
        # Cursor anzeigen lassen.
        display.curser()

        # 5 Sekunden warten
        time.sleep(5.0)
        # Cursor blinken lassen
        display.curser_blinken()

        # 5 Sekunden warten, den blinkenden Cursor stoppen und Cursor ausblenden
        time.sleep(5)
        display.curser_aus()  # nur bei blinkenden?
        # Nachricht von Rechts/Links scrollen lassen.
        display.nachricht_scroll("<-- Scroll -->")

        # Hintergrundbeleuchtung an und ausschalten.
        display.lcd.clear()
        display.lcd.message = "Flash backlight\nin 5 seconds..."
        time.sleep(5.0)
        # Hintergrundbeleuchtung ausschalten.
        display.hintergrund_blinken()
        # Nachricht ändern.
        display.nachricht("Goodbye")
        # Hintergrundbeleuchtung einschalten.
        display.hintergundbeleuchtung_an()
        # Hintergrundbeleuchtung ausschalten.
        time.sleep(2.0)
        display.hintergund_aus()

    except KeyboardInterrupt:
        # LCD ausschalten.
        display.hintergund_aus()

if __name__ == '__main__':
    main()