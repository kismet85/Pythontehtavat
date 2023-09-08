# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random
def noppa(tahkojenmaara):
    return random.randint(1, tahkojenmaara)

def main():
    noppasumma = 0
    maxSilmaLuku = int(input("Syötä maksimisilmäluku: \n"))
    while noppasumma<maxSilmaLuku:
        noppa1 = noppa(maxSilmaLuku)
        print(f"Nopanarvo on {noppa1}")
        noppasumma += noppa1
        if noppasumma >= maxSilmaLuku:
            print(f"Noppien summa on {noppasumma}")
            break

main()