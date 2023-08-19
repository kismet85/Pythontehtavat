import random
kolmeNumSarjaLista = []
neliNumSarjaLista = []
for i in range(0,3):
    num = random.randint(0,9)
    kolmeNumSarjaLista.append(num)

for i in range(0,4):
    num = random.randint(1,6)
    neliNumSarjaLista.append(num)

kolmenumsarja = ''.join(str(item) for item in kolmeNumSarjaLista)
nelinumsarja = ''.join(str(item) for item in neliNumSarjaLista)
print(kolmenumsarja)
print(nelinumsarja)