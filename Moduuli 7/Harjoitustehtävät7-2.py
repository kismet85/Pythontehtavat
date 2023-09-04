# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa.
# Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.

nimet = set()

def nimikysely():
    nimi = input("Syötä nimi: \n")

    while nimi!="":
        for nimijoukko in nimet:
            if nimijoukko!=nimi:
                print("Uusi nimi.")
                break
            elif nimijoukko==nimi:
                print("Nimi syötettiin jo. ")
        nimet.add(nimi)
        nimi = input("Syötä nimi: \n")

def main():
    nimikysely()
    for nimiarvaus in nimet:
        print(nimiarvaus)

main()
