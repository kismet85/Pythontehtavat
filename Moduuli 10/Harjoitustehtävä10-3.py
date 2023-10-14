"""

Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki hissit pohjakerrokseen.
Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

"""

class Hissi:

    def __init__(self,alin_kerros,ylin_kerros):
        self.ylin_kerros = ylin_kerros
        self.alin_kerros = alin_kerros
        self.kerros = 1

    def kerros_ylös(self,kerros):
        if self.kerros + 1 >10:
            self.ylin_kerros = 10
        else:
            for kerros in range(0, kerros):
                self.kerros += 1
                print(f"matkustit hissillä kerroksen ylemmäs")
                print(f"Olet kerroksessa {self.kerros}")
    def kerros_alas(self,kerros):
        if self.kerros - 1 < 1:
            self.alin_kerros = 1
        else:
            for kerros in range(0,kerros):
                self.kerros -= 1
                print(f"matkustit hissillä kerroksen alemmas")
                print(f"Olet kerroksessa {self.kerros}")
    def siirry_kerrokseen(self,kerroksia):
        if self.kerros == kerroksia:
            print("Olet jo kohteessa")
        elif self.kerros > kerroksia:
            for kerros in range(kerroksia,self.kerros):
                self.kerros_alas(1)
        else:
            for kerros in range(1, kerroksia):
                self.kerros_ylös(1)


class Talo:

    hissit = []
    def __init__(self,alin_kerros,ylin_kerros,hissi_lukumaara):
        self.ylin_kerros = ylin_kerros
        self.alin_kerros = alin_kerros
        self.hissi_lukumaara = hissi_lukumaara
        self.kerros = 1

        for i in range(hissi_lukumaara):
            self.hissit.append(Hissi(1, 10))

    def aja_hissia(self, hissin_numero, kohdekerros):
        hissi = self.hissit[hissin_numero - 1]

        if kohdekerros > hissi.ylin_kerros:
            print("Kohdekerros on talon yläpuolella")
        elif kohdekerros < hissi.alin_kerros:
            print("Kohdekerros on talon alapuolella")
        else:
            print(f"Hissi numero {hissin_numero}")
            hissi.siirry_kerrokseen(kohdekerros)

    def palohälytys(self):
        for i in range(len(self.hissit)):
            print(f"------------------------")
            print(f"PALOHÄLYTYS, hissi siirtyvät pohjakerrokseen!")
            talo.aja_hissia(i+1,1)


talo = Talo(1, 10, 2)


talo.aja_hissia(1, 5)
print(f"------------------------")
talo.aja_hissia(2, 5)
talo.palohälytys()
