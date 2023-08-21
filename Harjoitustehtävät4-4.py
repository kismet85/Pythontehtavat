import random
randomLuku = random.randint(1, 10)

arvaus = int(input("Arvaa luku 1 - 10 väliltä. \n"))

while arvaus != randomLuku:
    if arvaus < randomLuku:
        print("Liian pieni arvaus")
        arvaus = int(input("Arvaa luku 1 - 10 väliltä. \n"))
    elif arvaus > randomLuku:
        print("Liian suuri arvaus")
        arvaus = int(input("Arvaa luku 1 - 10 väliltä. \n"))
    else:
        break
print("Oikein.")