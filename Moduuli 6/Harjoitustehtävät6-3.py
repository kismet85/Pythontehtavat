# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän. Yksi gallona on 3,785 litraa.

def laskeGallonat(gallonat):
    litra = gallonat*3.785
    print(f"Syöttämäsi gallonamäärä on litroina {litra}")
    return

def main():
    gallonaMaara = float((input("Syötä gallonamäärä: \n")))
    while gallonaMaara!=0:
        if gallonaMaara>0:
            laskeGallonat(gallonaMaara)
            gallonaMaara = float((input("Syötä gallonamäärä: \n")))
        else:
            break
    print("Syötit pienemmän määrän kuin 0.")

main()