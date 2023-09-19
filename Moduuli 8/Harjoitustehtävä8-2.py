# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

import mysql.connector
import re
def kysynta():
    maakoodiSyote = input("Syötä maakoodi(Esim. FI): \n")
    while maakoodiSyote!="":
        haettava = haeLentokenttaICAO(maakoodiSyote)
        print(f"{haettava[0],haettava[1] ,haettava[2],haettava[3],haettava[4]}")
        maakoodiSyote = input("Syötä maakoodi(Esim. FI): \n")



def haeLentokenttaICAO(lentokentta):
    sql = ("SELECT type, COUNT(type) as amount FROM airport WHERE iso_country = %s GROUP BY type")
    kursori = yhteys.cursor()
    kursori.execute(sql, (lentokentta,))
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        return tulos

# Pääohjelma
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='ismet',
         password='kismet',
         autocommit=True
         )

kysynta()