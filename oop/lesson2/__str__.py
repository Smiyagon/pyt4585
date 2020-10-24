class Personel:
    Adi = ""
    Soyadi = ""
    Telefon = ""
    Mail = ""
    Yas = 0

    def  __str__(self): # __str__ metodu üzerine yazma metodudur ram bilgisi yerine bizim yazıcağımız bilgileri verir. 
        return f"{self.Adi} {self.Soyadi}"

personel = Personel()
personel.Adi = "Tarık"
personel.Soyadi = "Kotan"
personel.Telefon = "05340886128"
personel.Mail = "tarik.kotan@hotmail.com"
personel.Yas = 10

print(personel) # ram üzerindeki adresi verir. 

