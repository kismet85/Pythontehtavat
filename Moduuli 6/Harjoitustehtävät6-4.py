# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

lukulista = []

def summa(lukulista):
    summa = 0
    lista = lukulista
    for luku in lista:
        summa = summa + luku
    return print(f"Lukujen yhteinen summa on: {summa}")
def main():
    while True:
        luku = input("Syötä luku. \n")
        if luku!="":
            lukulista.append(int(luku))
        else:
            break

    summa(lukulista)

main()


