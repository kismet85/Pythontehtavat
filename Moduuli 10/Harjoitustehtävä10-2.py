"""

Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.
Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

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


talo = Talo(1, 10, 3)


talo.aja_hissia(1, 5)
print(f"------------------------")
talo.aja_hissia(1, 5)
print(f"------------------------")
talo.aja_hissia(2, 6)

