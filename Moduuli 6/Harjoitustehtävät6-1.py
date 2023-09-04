# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma,
# joka heittää noppaa niin kauan kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
import random
def noppa():
    return random.randint(1, 6)

def main():
    noppa1 = 0
    while noppa1 != 6:
        noppa1 = noppa()
        print(f"Nopanarvo on {noppa1}")

main()