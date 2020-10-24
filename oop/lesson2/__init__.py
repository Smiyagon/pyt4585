# __init__ constructor (yapıcı metod) olarak geçer. Sınıftan bir örnek aldığınızda yapılması gereken konfigürasyon
# vs var ise __init__ iiçerisinde tanımlayabilirsiniz.

class Personel:

    Adi = ""
    Soyadi = ""
    Telefon = ""
    Mail = "" 


    def __str__(self):
        return f"{self.Adi} {self.Soyadi}"
    
    def __init__(self,adi,soyadi,telefon,mail):
        self.Adi = adi
        self.Soyadi = soyadi
        self.Telefon = telefon
        self.Mail = mail
        print("__init__ metodu çalıştı")
personel = Personel("Tarık","Kotan","05340886128","tarik.kotan@hotmail.com")
print(personel)
