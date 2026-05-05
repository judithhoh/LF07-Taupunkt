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
        steatment = 'CREATE TABLE IF NOT EXISTS ' + tabelle + '(id INTEGER PRIMARY KEY AUTOINCREMENT,' + spalten + ')'
        self.cursor.execute(steatment)
    def daten_einfuegen(self, tabelle, parameter, values):
        # 3. Daten einfügen
        statement = "INSERT INTO "+tabelle+" ("+parameter+") VALUES ("+values+")"
        #print(statement)
        self.cursor.execute(statement)
        self.conn.commit() # Änderungen speichern
    def schliessen(self):
        # 4. Verbindung schließen
        self.conn.close()
    def abfrage(self, tabelle):
        # Daten abfragen
        self.cursor.execute("SELECT * FROM "+tabelle)
        print("Tabellen inhalt")
        for row in self.cursor.fetchall():
            print(row)

def main():
   test = sqlite_datenbank
   test.verbinden(test,'Daten')
   test.tabelle_erstellen(test, "Daten","temp INTEGER, humytity INTEGER, timestamp TEXT")
   test.daten_einfuegen(test, "Daten", "temp, humytity, timestamp", "15, 20, datetime('now')")
   test.abfrage(test, "Daten")
   test.schliessen(test)

if __name__ == '__main__':
    main()