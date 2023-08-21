pienin = 100000
suurin = 0

while True:
    luku = input("Syötä luku: \n")
    if(luku==""):
        break
    if int(luku) < int(pienin):
        pienin = luku
    if int(luku) > int(suurin):
        suurin = luku
print(f"Pienin luku on {pienin} ja suurin luku on {suurin}")
