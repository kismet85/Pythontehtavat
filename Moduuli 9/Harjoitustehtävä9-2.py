"""
Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h,
sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
Kuljettua matkaa ei tarvitse vielä päivittää.

"""

class Auto:
    def __init__(self,rekisteritunnus,huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.hetken_nopeus = 0
        self.matka = 0

    def kiihdyta(self,kiihdytys):
        if self.hetken_nopeus + kiihdytys > self.huippunopeus:
            self.hetken_nopeus = self.huippunopeus
        elif self.hetken_nopeus + kiihdytys < 0:
            self.hetken_nopeus = 0
        else:
            self.hetken_nopeus += kiihdytys

    def print_car(self):
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("Rekisteritunnus:", self.rekisteritunnus)
        print("Huippunopeus:", self.huippunopeus, "km/h")
        print("Tämänhetkinen nopeus:", self.hetken_nopeus, "km/h")
        print("Kuljettu matka:", self.matka, "km")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")

Lada = Auto("ABC-123", 142)
Lada.print_car()
print(f"Auto kiihdyttää 30km/h lisää nopeutta")
Lada.kiihdyta(30)
Lada.print_car()
print(f"Auto kiihdyttää 70km/h lisää nopeutta")
Lada.kiihdyta(70)
Lada.print_car()
print(f"Auto kiihdyttää 50km/h lisää nopeutta, mutta saavuttaa huippunopeuden")
Lada.kiihdyta(50)
Lada.print_car()
print(f"Auto jarruttaa!")
Lada.kiihdyta(-200)
Lada.print_car()
