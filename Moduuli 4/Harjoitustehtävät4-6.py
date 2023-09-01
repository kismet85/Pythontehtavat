import random
muuttuja = 0

pisteidenmaara = int(input("Anna pisteiden määrä: "))

sisaluvut = 0

while True:
    if muuttuja == pisteidenmaara:
        print(str(4*sisaluvut/pisteidenmaara))
        break
    y = random.uniform(-1, 1)
    x = random.uniform(-1, 1)
    muuttuja += 1
    if((x**2) + (y**2) < 1):
        sisaluvut += 1