import sqlite3

class sqlite_datenbank:
    def __init__(self):
        self.cursor = None
        self.conn = None

    def verbinden(self, datei):
        # 1. Verbindung herstellen (wird erstellt, falls nicht vorhanden)
        self.conn = sqlite3.connect(datei+'.db')
        self.cursor = self.conn.cursor()

    def tabelle_erstellen(self, tabelle, spalten):
        # 2. Tabelle erstellen
        steatment = 'CREATE TABLE IF NOT EXISTS '+ tabelle +'(id INTEGER PRIMARY KEY AUTOINCREMENT,' + spalten+')'
        self.cursor.execute(steatment)
    def daten_einfuegen(self):
        # 3. Daten einfügen
        self.cursor.execute("INSERT INTO Daten (temp, humytity) VALUES (15, 10)")
        self.conn.commit() # Änderungen speichern
    def schliessen(self):
        # 4. Verbindung schließen
        self.conn.close()
    def abfrage(self, tabelle):
        # Daten abfragen
        self.cursor.execute("SELECT * FROM "+tabelle)
        for row in self.cursor.fetchall():
            print(row)
