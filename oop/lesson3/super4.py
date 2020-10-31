class Personel():

    _baslangic_maas = 4000
    def __init__(self,ad,soyad,telefon):
        self.ad = ad
        self.soyad = soyad 
        self.telefon = telefon

    def FullName(self):
        return f"{self.ad} {self.soyad}"

    def Phone(self):
        return f" +90{self.telefon}"

    def __str__(self):
        return f"{self.ad} {self.soyad} {self.telefon} {self._baslangic_maas} "


# per = Personel("Tarık","Kotan","5340886128")
# print(per)
# print(per.Phone())

class Developer(Personel):
    _baslangic_maas = 7000
    def __init__(self,ad,soyad,telefon,yazilimdili):
        super().__init__(ad,soyad,telefon)
        self.yazilimdili = yazilimdili
    
    def __str__(self):
        return f"{super().__str__()} {self.yazilimdili} "

dev = Developer("Tarık","Kotan","05340886128","Python")

print(dev)