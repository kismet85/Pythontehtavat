# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
# kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math


def main():
    kutsuttu = 1
    while True:
        pizzaHalkaisija1 = input("Syötä ensimmäisen pizzan halkaisija: \n")
        pizzaHalkaisija2 = input("Syötä toisen pizzan halkaisija: \n")
        pizzaHinta1 = input("Syötä ensimmäisen pizzan hinta: \n")
        pizzaHinta2 = input("Syötä toisen pizzan hinta: \n")
        if pizzaHalkaisija1 !="" and pizzaHalkaisija2 !="" and pizzaHinta1 !="" and pizzaHinta2 !="":
            pizza1 = yksikkoHinta(float(pizzaHalkaisija1), float(pizzaHinta1), kutsuttu)
            kutsuttu +=1
            pizza2 = yksikkoHinta(float(pizzaHalkaisija2), float(pizzaHinta2), kutsuttu)

def yksikkoHinta(halkaisija, hinta,kutsuttu):

    area = (math.pi * (((halkaisija/100) / 2) ** 2))
    yksikkohinta=hinta/area
    hinta = float(round(yksikkohinta, 2))
    print(f"Pizza {kutsuttu} hinta on {hinta} euroa per neliömetri.")



main()



