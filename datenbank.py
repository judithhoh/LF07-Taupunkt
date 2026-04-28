import sqlite3

class sqlite_datenbank:
    def __init__(self):
        self.cursor = None
        self.conn = None

    def verbinden(self):
        # 1. Verbindung herstellen (wird erstellt, falls nicht vorhanden)
        self.conn = sqlite3.connect('test.db')
        self.cursor = self.conn.cursor()

    def tabelle_erstellen(self):
        # 2. Tabelle erstellen
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Daten (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                temp INTEGER,
                humytity INTEGER
            )
        ''')
    def daten_einfuegen(self):
        # 3. Daten einfügen
        self.cursor.execute("INSERT INTO Daten (temp, humytity) VALUES (15, 10)")
        self.conn.commit() # Änderungen speichern
    def schliessen(self):
        # 4. Verbindung schließen
        self.conn.close()
    def abfrage(self):
        # Daten abfragen
        self.cursor.execute("SELECT * FROM Daten")
        for row in self.cursor.fetchall():
            print(row)
