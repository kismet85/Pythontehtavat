# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

kevät = ("maaliskuu", "huhtikuu", "toukokuu")
kesä = ("kesäkuu", "heinäkuu", "elokuu")
syksy = ("syyskuu", "lokakuu", "marraskuu")
talvi = ("joulukuu", "tammikuu", "helmikuu")


while True:
    kuukausi = int(input("Syötä kuukausi: \n"))
    if kuukausi==12 or kuukausi==1 or kuukausi==2:
        print(f"talvi")
    elif kuukausi==3 or kuukausi==4 or kuukausi==5:
        print(f"kevät")
    elif kuukausi==6 or kuukausi==7 or kuukausi==8:
        print(f"kesä")
    elif kuukausi==9 or kuukausi==10 or kuukausi==11:
        print(f"syksy")
    else:
        break