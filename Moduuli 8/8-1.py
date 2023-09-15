# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja
# sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta. ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

import mysql.connector
import re
def kysynta():
    icaoSyote = input("Syötä aseman ICAO koodi: \n")
    while icaoSyote!="":
        haettava = haeLentokenttaICAO(icaoSyote)
        haettava = re.sub(r"\((.*?)\)", r"\1", haettava)
        haettava = haettava.strip("[]")
        print(f"Haettava lentokenttä ja paikkakunta: {haettava}")
        icaoSyote = input("Syötä aseman ICAO koodi: \n")



def haeLentokenttaICAO(lentokentta):
    sql = "SELECT name,municipality FROM airport"
    sql += " WHERE ident='" + lentokentta + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        return str(tulos)

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