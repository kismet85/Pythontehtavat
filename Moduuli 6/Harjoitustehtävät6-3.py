# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän. Yksi gallona on 3,785 litraa.

def laskeGallonat(gallonat):
    litra = gallonat*3.785
    print(f"Syöttämäsi gallonamäärä on litroina {litra}")
    return

def main():
    while True:
        gallonaMaara = float((input("Syötä gallonamäärä: \n")))
        if gallonaMaara>0:
            laskeGallonat(gallonaMaara)
        else:
            break
    print("Syötit pienemmän määrän kuin 0.")
main()