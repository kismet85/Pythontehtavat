# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen listan,
# joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

lukulista = []
def summa(lukulista):
    paritonLista = []
    for luku in lukulista:
        if luku%2!=0:
           paritonLista.append(luku)
    print(f"Lista missä on kaikki luvut: {lukulista}")
    print(f"Lista missä on parittomat luvut {paritonLista}")
    return
def main():
    luku = input("Syötä luku. \n")
    while luku!="":
        if luku!="":
            lukulista.append(int(luku))
            luku = input("Syötä luku. \n")
        else:
            break

    summa(lukulista)

main()