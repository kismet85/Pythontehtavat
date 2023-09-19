# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
# Laskenta perustuu tietokannasta haettuihin koordinaatteihin. Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
# Asenna kirjasto valitsemalla View / Tool Windows / Python Packages. Kirjoita hakukenttään geopy ja vie asennus loppuun.

import mysql.connector
from geopy.distance import geodesic as GD




def kysynta():
    maakoodiSyote1 = input("Syötä ICAO koodi ensimmäiselle lentokentälle: \n")
    maakoodiSyote2 = input("Syötä ICAO koodi toiselle lentokentälle: \n")
    while maakoodiSyote1!="" and maakoodiSyote2!="":
        haettava1 = haeLentokenttaICAO(maakoodiSyote1)
        haettava2 = haeLentokenttaICAO(maakoodiSyote2)
        print(f"Lentokentän {maakoodiSyote1} ja {maakoodiSyote2} etäisyys on:", round(GD(haettava1,haettava2).km))
        maakoodiSyote1 = input("Syötä ICAO koodi ensimmäiselle lentokentälle: \n")
        maakoodiSyote2 = input("Syötä ICAO koodi toiselle lentokentälle: \n")



def haeLentokenttaICAO(lentokentta):
    sql = ("SELECT latitude_deg,longitude_deg FROM airport WHERE ident= " + "'" + lentokentta + "'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
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