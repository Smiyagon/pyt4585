class Ogrenci:
    Adi = ""

    def NotVer(self,arg):
        print(self.Adi, f"adlı öğrenciye {arg} notu verildi.")

    def CezaVer(self,arg):
        print(self.Adi, f"adlı öğrenciye {arg} cezası verildi.")

    def YoklamaGirisi(self,arg):
        print(self.Adi, f"adlı öğrenci derse {arg}.")



ogrenci = Ogrenci()
ogrenci.Adi = "Tarık"
ogrenci.NotVer(20)
ogrenci.CezaVer("Disiplin")
ogrenci.YoklamaGirisi("girdi")
