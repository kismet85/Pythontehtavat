"""

Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.
Polttomoottoriauton ominaisuutena on bensatankin koko litroina. Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen,
huippunopeuden ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa. Kirjoita pääohjelma,
jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus,
käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.

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

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus,akkukapasiteetti):
        super().__init__(rekisteritunnus,huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti
        self.nopeus = 0
        self.matka = 0


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus,bensatankki):
        super().__init__(rekisteritunnus,huippunopeus)
        self.bensatankki = bensatankki
        self.nopeus = 0
        self.matka = 0


class Kilpailu:
    def __init__(self, nimi, autolista,tuntimäärä):
        self.nimi = nimi
        self.autolista = autolista
        self.tuntimäärä = tuntimäärä

    def tunti_kuluu(self):
        self.tuntimäärä -= 1
        for auto in self.autolista:
            muutos = random.randint(-20, 50)
            auto.kiihdyta(muutos)
            auto.kulje(1)


    def tulosta_tilanne(self):
        print("Rekisteritunnus   | Huippunopeus | Nopeus  | Matka")
        print("----------------------------------------------------")
        for auto in self.autolista:
            print(f"{auto.rekisteritunnus} ------------>| {auto.huippunopeus} km/h | {auto.nopeus} km/h | {auto.matka} km")
        print("----------------------------------------------------")

    def kilpailu_ohi(self):
        if self.tuntimäärä == 0:
            return True
        return False

def main():
    autolista =[]
    sähköauto = Sähköauto("ABC-155", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)
    autolista.append(sähköauto)
    autolista.append(polttomoottoriauto)

    kilpailu = Kilpailu("Sähkö vs Polttomoottori", autolista,3)
    print(f"Kilpailu {kilpailu.nimi} alkaa, kilpailussa on {len(kilpailu.autolista)} autoa.")
    kilpailu_loppuu = False
    while not kilpailu_loppuu:
        kilpailu.tunti_kuluu()
        kilpailu.tulosta_tilanne()
        kilpailu_loppuu = kilpailu.kilpailu_ohi()



if __name__ == "__main__":
    main()
