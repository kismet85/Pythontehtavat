import random

nopat = []
summa = 0
heittokerrat = 0
lukumaara = int(input("Anna arpakuutioiden lukumäärä: \n"))
while heittokerrat<lukumaara:
    silmaluku = random.randint(1, 6)
    nopat.append(silmaluku)
    heittokerrat +=1

for noppa in nopat:
    summa += noppa

print(summa)