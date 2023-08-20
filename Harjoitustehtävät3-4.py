vuosi = int(input("Syötä vuosi: \n"))

if (vuosi % 400 == 0) and (vuosi % 100 == 0):
    print(f"vuosi {vuosi} on karkausvuosi.")
elif (vuosi % 4 == 0) and (vuosi % 100 != 0):
    print(f"vuosi {vuosi} on karkausvuosi.")
else:
    print(f"vuosi 0{vuosi} ei ole karkausvuosi.")