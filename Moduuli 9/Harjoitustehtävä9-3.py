"""

Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

"""

class Auto:
    def __init__(self,rekisteritunnus,huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.hetken_nopeus = 0
        self.matka = 2000

    def kiihdyta(self,kiihdytys):
        if self.hetken_nopeus + kiihdytys > self.huippunopeus:
            self.hetken_nopeus = self.huippunopeus
        elif self.hetken_nopeus + kiihdytys < 0:
            self.hetken_nopeus = 0
        else:
            self.hetken_nopeus += kiihdytys
    def kulje(self,tunti_maara):
        matka_tunnissa = self.hetken_nopeus * tunti_maara
        self.matka = self.matka + int(matka_tunnissa)

    def print_car(self):
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("Rekisteritunnus:", self.rekisteritunnus)
        print("Huippunopeus:", self.huippunopeus, "km/h")
        print("Tämänhetkinen nopeus:", self.hetken_nopeus, "km/h")
        print("Kuljettu matka:", self.matka, "km")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")

Lada = Auto("ABC-123", 142)
Lada.print_car()
print(f"Auto kiihdyttää 60km/h lisää nopeutta")
Lada.kiihdyta(60)
Lada.kulje(1.5)
Lada.print_car()
