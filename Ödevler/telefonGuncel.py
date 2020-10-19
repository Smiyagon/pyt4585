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
        pass

    def arama(self):
        pass

kisiler = Kisiler("","","","")
kisiler.kayitEkle("Ahmet","semsi","ahmet.semsi@hotmail.com","02165458545")