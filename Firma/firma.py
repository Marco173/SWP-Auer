class Firma:
        def __init__(self, firmenname, firmenadresse, firmenbuchnummer):
            self.firmenname = firmenname
            self.firmenadresse = firmenadresse
            self.firmenbuchnummer = firmenbuchnummer
            self.abteilungen = []



        def totalangestellte(self):
            total = 0
            for abteilung  in self.abteilungen:
                total += abteilung.mitarbeiter.__len__()
            return total

        def totalchef(self):
            return len(self.abteilungen)

        def statistics(self):
            m = 0
            w = 0
            for abteilung in self.abteilungen:
                for mitarbeiter in abteilung.mitarbeiter:
                    if mitarbeiter.geschlecht == "m":
                        m += 1
                    else:
                        w += 1
            return [{"m": round(m / self.totalangestellte() * 100,1), "w": round(w / self.totalangestellte() * 100, 1)}]

        def AbteilungmitmeistenMitarbeiter(self):
            abteilung_max_mitarbeiter = max(self.abteilungen, key=lambda x: x.anzahlMitarbeiter())
            return abteilung_max_mitarbeiter.abteilungsname, abteilung_max_mitarbeiter.anzahlMitarbeiter()

        def __str__(self):
            return "Firmenname" +self.firmenname+"\nFirmenadresse"+self.firmenadresse+"\nFirmennummer"\
                +self.firmennummer

class Abteilung:
        def __init__(self, abteilungsname, firma):
            self.abteilungsname = abteilungsname
            self.abteilungsleiter = None
            self.mitarbeiter = []
            self.firma = firma
            firma.abteilungen.append(self)

        def anzahlMitarbeiter(self):
            return len(self.mitarbeiter)

        def __str__(self):
            return "\nAbteilungsname: " + self.abteilungsname + "\nAbteilungsleiter: " + self.abteilungsleiter.__str__() + "\nMitarbeiter: " + (self.mitarbeiter).__str__()


class Person:
        def __init__(self,vorname,nachname,alter, geschlecht):
            self.vorname = vorname
            self.nachname = nachname
            self.alter = alter
            self.geschlecht = geschlecht

        def __str__(self):
            return "\n\n\tVorname: " + self.vorname + "\n\tNachname: " + self.nachname + "\n\tAlter: " + str(
                self.alter) + "\n\tGeschlecht: " + self.geschlecht



class Mitarbeiter(Person):
        def __init__(self,vorname,nachname,alter,geschlecht,gehalt,abteilung):
            super().__init__(vorname,nachname,alter,geschlecht)
            self.gehalt = gehalt
            self.abteilung = abteilung
            self.abteilung.mitarbeiter.append(self)

        def __repr__(self):
            return self.__str__()
        def __str__(self):
            return super().__str__() + "\n\tgehalt: " +str(self.gehalt)

class Abteilungsleiter(Mitarbeiter):
        def __init__(self, vorname, nachname, alter, geschlecht, gehalt, abteilung):
            super().__init__(vorname, nachname, alter, geschlecht, gehalt, abteilung)
            self.abteilung.abteilungsleiter = self

        def __str__(self):
            return super().__str__() +"\n"



if __name__ == '__main__':

        #create firma
        firma = Firma("Hoertnagl","Triendstraße 5","177423x")

        #create 3 Abteilungen
        abteilung1 = Abteilung("Zerlegung",firma)
        abteilung2 = Abteilung("Füllerei",firma)
        abteilung3 = Abteilung("Verpackung",firma)

        #create 3 Abteilungsleiter
        Abteilungsleiter1 = Abteilungsleiter("Max","Mustermann", 26,"m",3200,abteilung1)
        Abteilungsleiter2 = Abteilungsleiter("Benedikt" ,"Schmid", 40,"m",4470,abteilung1)
        Abteilungsleiter3 = Abteilungsleiter("Michaela", "Plattner", 60, "w", 5500, abteilung2)

        #create 3 mitarbeiter
        mitarbeiter1 = Mitarbeiter("Andreas","Plank",24,"m",2000, abteilung1)
        mitarbeiter2 = Mitarbeiter("Michael","Flink",60,"w",2300,abteilung1)
        mitarbeiter3 = Mitarbeiter("Daniel","Huber",37,"m",1870,abteilung2)
        mitarbeiter4 = Mitarbeiter("Marco", "Auer", 19, "m", 1870, abteilung3)
        mitarbeiter5 = Mitarbeiter("Valentina", "Klausner", 56, "w", 2300, abteilung3)
        mitarbeiter6 = Mitarbeiter("Carlos", "Jasel", 45, "m", 2540, abteilung3)

        #Abfragen:
        print(firma.firmenname)
        print(abteilung1)
        print("\n")
        print("Gesamt-Angestellte:")
        print(firma.totalangestellte())
        print("Gesamt-Chefs:")
        print(firma.totalchef())
        print("Anzahl an Abteilungen:")
        print(firma.abteilungen.__len__())
        print("Prozentanteil: Frauen/Männer")
        print(firma.statistics())
        print(firma.AbteilungmitmeistenMitarbeiter())


