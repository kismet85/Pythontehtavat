# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
# hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)


asematLista = []
icaoLista = []

def lisays(icao,asema):
    icaoLista.append(icao)
    asematLista.append(asema)
def haku(haettavaIcao):
    index = 0
    for item in icaoLista:
        if haettavaIcao== item:
            print(f"ICAO on {item}")
            print(f"Haettava lentokenttä on: {asematLista[index]}")
        index += 1


kaytossa = True
def main():

    while kaytossa:
        kysymys = input("Haluatko syöttää uuden lentoaseman, hakea listalta lentoasema vai lopettaa? \n1=Uusi lentoasema \n2=Hakea lentoasema listalta \n3=lopettaa. \n")
        if kysymys == "1":
            icaoSyote = input("Syötä aseman ICAO koodi: \n")
            asemaNimi = input("Syötä aseman nimi. \n")
            lisays(icaoSyote,asemaNimi)
        elif kysymys == "2":
            icaoHaku = input("Syötä haettava asema ICAO koodin avulla. \n")
            haku(icaoHaku)
        elif kysymys == "3":
            print("Lopetit lentoasemien haun.")
            break
        else:
            print("Väärä syöte")

main()