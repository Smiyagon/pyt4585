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
        f = open("kisiler.txt","a+")
        self.ad = ad
        self.soyad = soyad
        self.telefon = telefon
        self.mail = mail
        f.write(f"{ad},{soyad},{mail},{telefon}\n")
        print(f"{ad} {soyad} kişisi rehbere eklendi.")

    def kayitGuncelleme(self):
        pass

    def kayitSilmek(self):
        pass

    def kayitGosterme(self):
        o = open("kisiler.txt","r")
        for i in o:
            print(i)
        o.close()

    def arama(self):
        pass

isim = input("Kişinin adını giriniz : ")
soyad = input("Kişinin soyadını giriniz : ")
mail = input("Kişinin mail adresini giriniz : ")
telefon = input("Kişinin telefon numarasını giriniz : ")

kisiler = Kisiler("","","","")
kisiler.kayitEkle(isim,soyad,mail,telefon)
kisiler.kayitGosterme()