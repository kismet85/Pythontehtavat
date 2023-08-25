# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma,
# joka heittää noppaa niin kauan kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
import random

nopanhaku = 6

while True:
    nopanarvo = random.randint(1,6)
    print(f"Nopanarvo on {nopanarvo}")
    if(nopanarvo==6):
        break
