"""

Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron. Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas.
 Uusi hissi on aina alimmassa kerroksessa. Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
 metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
 Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
 Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

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

    def siirry_kerrokseen(self, kerroksia):
        if self.kerros == kerroksia:
            print("Olet jo kohteessa")
        elif self.kerros > kerroksia:
            for kerros in range(kerroksia, self.kerros):
                self.kerros_alas(1)
        else:
            for kerros in range(1, kerroksia):
                self.kerros_ylös(1)


hissi = Hissi(1,10)
hissi.siirry_kerrokseen(5)
print("----------------")
hissi.siirry_kerrokseen(1)
print("----------------")
hissi.siirry_kerrokseen(10)
print("----------------")
hissi.siirry_kerrokseen(4)
print("----------------")
hissi.siirry_kerrokseen(1)
print("----------------")
hissi.siirry_kerrokseen(9)
print("----------------")


