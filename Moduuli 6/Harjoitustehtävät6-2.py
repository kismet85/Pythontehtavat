# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

nopanhaku = 6
noppasumma = 0
while True:
    nopanarvo = random.randint(1,6)
    print(f"Nopanarvo on {nopanarvo}")
    noppasumma += nopanarvo
    if(noppasumma==21):
        break
