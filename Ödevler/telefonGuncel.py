import os


class  Kisiler():
    ad = ""
    soyad = ""
    mail = ""
    telefon = ""
    
    def __init__(self,ad,soyad,mail,telefon):
        self.ad = ad
        self.soyad = soyad
        self.mail = mail
        self.telefon = telefon
        
    def kayitEkle(self,ad,soyad,mail,telefon):
        os.system("cls")
        f = open("kisiler.txt","a")
        self.ad = ad
        self.soyad = soyad
        self.telefon = telefon
        self.mail = mail
        f.write(f"{ad},{soyad},{mail},{telefon}\n")
        print(f"{ad} {soyad} kişisi rehbere eklendi.\n")

    def kayitGuncelleme(self):
        pass

    def kayitSilmek(self):
        pass

    def kayitGosterme(self):
        os.system("cls")
        o = open("kisiler.txt","r")
        for i in o:
            print(i)
        o.close()

    def arama(self):
        pass

isim = input("Kişinin adını giriniz : ").upper().replace("ı","i").replace("ğ","g").replace("İ","I").replace("ö","o").replace("ş","s").replace("Ş","S").replace("Ö","O").replace("Ğ","G").replace("Ü","U").replace("ü","u").replace("ç","c").replace("Ç","C")
soyad = input("Kişinin soyadını giriniz : ").upper().replace("ı","i").replace("ğ","g").replace("İ","I").replace("ö","o").replace("ş","s").replace("Ş","S").replace("Ö","O").replace("Ğ","G").replace("Ü","U").replace("ü","u").replace("ç","c").replace("Ç","C")
mail = input("Kişinin mail adresini giriniz : ").lower().replace("ı","i").replace("ğ","g").replace("İ","I").replace("ö","o").replace("ş","s").replace("Ş","S").replace("Ö","O").replace("Ğ","G").replace("Ü","U").replace("ü","u").replace("ç","c").replace("Ç","C")
telefon = input("Kişinin telefon numarasını giriniz : ")

kisiler = Kisiler("","","","")
kisiler.kayitEkle(isim,soyad,mail,telefon)
kisiler.kayitGosterme()