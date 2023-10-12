"""
Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja,
joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin. Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h). Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.
"""

class Auto:
    def __init__(self,rekisteritunnus,huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.hetken_nopeus = 0
        self.matka = 0

    def print_car(self):
        print("Rekisteritunnus:", self.rekisteritunnus)
        print("Huippunopeus:", self.huippunopeus, "km/h")
        print("Tämänhetkinen nopeus:", self.hetken_nopeus, "km/h")
        print("Kuljettu matka:", self.matka, "km")

Lada = Auto("ABC-123", 142)
Lada.print_car()

