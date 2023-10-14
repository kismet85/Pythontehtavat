"""

Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista.
Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli arpoo kunkin auton nopeuden muutoksen ja
kutsuu kullekin autolle kulje-metodia.
tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.
Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli". Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.

"""

import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunti_maara):
        matka_tunnissa = self.nopeus * tunti_maara
        self.matka = self.matka + int(matka_tunnissa)

class Kilpailu:
    def __init__(self, nimi, pituus_km, autolista):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autolista = autolista

    def tunti_kuluu(self):
        for auto in self.autolista:
            muutos = random.randint(-20, 20)
            auto.kiihdyta(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print("Rekisteritunnus    | Huippunopeus | Nopeus       | Matka")
        print("----------------------------------------------------")
        for auto in self.autolista:
            print(f"{auto.rekisteritunnus} ------------>| {auto.huippunopeus} km/h | {auto.nopeus} km/h | {auto.matka} km")
        print("----------------------------------------------------")

    def kilpailu_ohi(self):
        for auto in self.autolista:
            if auto.matka >= self.pituus_km:
                return True
        return False

def main():
    autolista = []
    for i in range(10):
        auto = Auto(f"ABC-{i+1}", random.randint(100, 200))
        autolista.append(auto)

    kilpailu = Kilpailu("Suuri romuralli", 8000, autolista)
    print(f"Kilpailu {kilpailu.nimi} alkaa, kilpailu on {kilpailu.pituus_km} km pitkä ja kilpailussa on {len(kilpailu.autolista)} autoa.")
    kilpailu_loppuu = False
    while not kilpailu_loppuu:
        kilpailu.tunti_kuluu()
        kilpailu.tulosta_tilanne()
        kilpailu_loppuu = kilpailu.kilpailu_ohi()

    print("Kilpailu ohi!")


if __name__ == "__main__":
    main()
