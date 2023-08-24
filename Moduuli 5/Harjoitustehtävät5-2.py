numerot = []

numba = input("Syötä luku: \n")
while numba!="":
    num1 = float(numba)
    numerot.append(num1)
    numerot.sort()
    numba = input("Syötä luku: \n")

maxList = sorted(numerot, reverse=True)
print(maxList[:5])