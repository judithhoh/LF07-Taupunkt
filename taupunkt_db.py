from datenbank import sqlite_datenbank

class taupunkt_db_class:
    def __init__(self):
        self.db = sqlite_datenbank
        self.datei = "Taupunkt"
        self.tabelle = "Daten"
        self.parameters = ["temperatur_innen", "luftfeuchtikeit_innen","temperatur_aussen", "luftfeuchtikeit_aussen",
                           "delta", "timestemp", "luefter", "taupunkt_innen", "taupunkt_aussen"]
        self.typen = ["INTEGER", "INTEGER","INTEGER", "INTEGER", "INTEGER", "TEXT", "BOOLEAN", "INTEGER", "INTEGER"]
        self.db.verbinden(self.db, self.datei)
        erstellen = (self.parameters[0] + " "+self.typen[0]+", "+self.parameters[1] + " "+self.typen[1]+", "+
                     self.parameters[2] + " "+self.typen[2]+", "+self.parameters[3] + " "+self.typen[3]+", "+
                     self.parameters[4] + " "+self.typen[4]+", "+self.parameters[5] + " "+self.typen[5]+", "+
                     self.parameters[6] + " "+self.typen[6]+", "+self.parameters[7] + " "+self.typen[7]+", "+
                     self.parameters[8] + " "+self.typen[8])
        self.db.tabelle_erstellen(self.db, self.tabelle, erstellen)

    def daten_schreiben(self, temperatur_innen, temperatur_aussen, luffeuchtikeit_innen, luffeuchtigkeit_aussen, delta,
                        luefter, taupunkt_inne, taupunkt_aussen):
        parameter = (self.parameters[0] + ", " + self.parameters[1] + ", " + self.parameters[2] + ", " +
                     self.parameters[3] + ", " + self.parameters[4] + ", " + self.parameters[5] + ", " +
                     self.parameters[6]+ ", " + self.parameters[7]+ ", " + self.parameters[8])
        values = (str(temperatur_innen) +", "+str(luffeuchtikeit_innen)+", "+str(temperatur_aussen)+", "+
                  str(luffeuchtigkeit_aussen) +", " +str(delta)+", datetime('new'), "+str(luefter)+", "+
                  str(taupunkt_inne)+", "+ str(taupunkt_aussen))
        self.db.daten_einfuegen(self.db, self.tabelle, parameter, values)

    def daten_lesen(self):
        self.db.abfrage(self.db, self.tabelle)

def main():
   test = taupunkt_db_class()
   test.daten_lesen(test)

if __name__ == '__main__':
    main()