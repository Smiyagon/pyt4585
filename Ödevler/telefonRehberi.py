kisiler = [
    {
        "İndex No": 0,
        "İsim" : "tarık",
        "Soyisim" : "kotan",
        "Mail Adresi":"kotan_t@hotmail.com",
        "Telefon Numarası" : "05340886128"
    },
    {
        "İndex No": 1,
        "İsim" : "ahmet",
        "Soyisim" : "nurcan",
        "Mail Adresi":"ahmet.nurcan@hotmail.com",
        "Telefon Numarası" : "05124587985"
    },
    {
        "İndex No": 2,
        "İsim" : "mehmet",
        "Soyisim" : "gürsel",
        "Mail Adresi":"mehmet.gürsel@hotmail.com",
        "Telefon Numarası" : "02164547895"
    },
    {
        "İndex No": 3,
        "İsim" : "devrim",
        "Soyisim" : "keser",
        "Mail Adresi":"devrim.keser@hotmail.com",
        "Telefon Numarası" : "02164547878"
    },
]

def ekleme():
    index = len(kisiler) - 1
    isim = input("İsim: ").lower()
    soyisim = input("Soyisim: ").lower()
    mail = input("Mail Adresi: ").lower()
    telefon = input("Telefon Numarası: ")
    kisiler.append({"İndex No:": index,"İsim" : isim,"Soyisim" : soyisim,"Mail Adresi":mail,"Telefon Numarası" : telefon})
    print(f"{isim} adlı kişi eklendi.")
    print("""
    ############################################
    #    Başka bir kişi eklemek için     (1)   #
    #    Ana ekrana dönmek için          (2)   #
    #    Uygulamadan çıkış yapmak için   (3)   #
    ############################################
    """)
    deger = int(input("Lütfen yapacağınız işlemin numarasını giriniz: "))
    if deger == 1:
        ekleme()
    elif deger == 2:
        anaekran()
    elif deger == 3:
        exit
    else:
        print("Lütfen düzgün bir değer giriniz!")
    

def anaEkranDonus():
    sonuc = input("Başka bir işlem yapmak istiyor musunuz ?(y/n): ").lower()
    if sonuc =="y":
        return anaekran()
    elif sonuc =="n":
        exit
    else:
        print("Sadece 'y' veya 'n' değerlerini giriniz")
        anaEkranDonus()

def guncellemeEkrandonus():
    sonuc = input("Başka bir güncelleme işlemi yapmak istiyor musunuz ?(y/n): ").lower()
    if sonuc =="y":
        return guncelleme()
    elif sonuc =="n":
        anaEkranDonus()
    else:
        print("Sadece 'y' veya 'n' değerlerini giriniz")
        guncellemeEkrandonus()

def kayitSilmeEkranDonus():
    sonuc = input("Başka bir kayıt silmek  istiyor musunuz ?(y/n): ").lower()

    if sonuc =="y":
        return kayitSilme()
    elif sonuc =="n":
        exit
    else:
        print("Sadece 'y' veya 'n' değerlerini giriniz")
        kayitSilmeEkranDonus()

def kayitSilme():
    deger = int(input("Lütfen silinecek kişinin adını giriniz: "))
    sonuc = input("Bu kişiyi silmek istediğinize emin misiniz?(y/n):").lower()
    if sonuc == "y":
        kisiler[deger].remove("İsim")
        print("Kişi silindi")
    elif sonuc == "n":
        print("Çıkış yapıldı")
        exit
    else:
        print("Lütfen düzgün bir değer giriniz")
        kayitSilme()

def kayitListesi():
    i = 0
    while i < len(kisiler):
        print(kisiler[i])
        i += 1


def guncelleme():
    print("""
    Yapacağınız güncellemede kişinin;
    Adını değiştirmek için              (1)
    Soyismini değiştirmek için          (2)
    Mail Adresini değiştirmek için      (3)
    Telefon Numarasını değiştirmek için (4)
    Ana ekrana dönmek için              (5)
    Uygulamadan çıkmak için             (6)
    """)
    deger = int(input("Lütfen yapacağınız işlemin numarasını giriniz : "))
    

    if deger == 1:
        guncellenecekIndex  = int(input("Kişinin index numarasını giriniz: "))
        guncellenecekKey    = "İsim"

        oldName = kisiler[guncellenecekIndex][guncellenecekKey]
        kisiler[guncellenecekIndex][guncellenecekKey] = input("Kişinin yeni adını giriniz: ")

        print("Kişinin Yeni Adı :", kisiler[guncellenecekIndex]["İsim"],"Olarak Güncellenmiştir")
        guncellemeEkrandonus()
        

    elif deger == 2:
        guncellenecekIndex  = int(input("Kişinin index numarasını giriniz: "))
        guncellenecekKey    = "Soyisim"

        oldName = kisiler[guncellenecekIndex][guncellenecekKey]
        kisiler[guncellenecekIndex][guncellenecekKey] = input("Kişinin yeni soyismini giriniz: ")

        print("Kişinin Yeni soyadı :",kisiler[guncellenecekIndex]["Soyisim"],"Olarak Güncellenmiştir")
        guncellemeEkrandonus()

    elif deger == 3:
        guncellenecekIndex  = int(input("Kişinin index numarasını giriniz: "))
        guncellenecekKey    = "Mail Adresi"

        oldName = kisiler[guncellenecekIndex][guncellenecekKey]
        kisiler[guncellenecekIndex][guncellenecekKey] = input("Kişinin yeni mail adresini giriniz: ")

        print("Kişinin yeni mail adresi :", kisiler[guncellenecekIndex]["Mail Adresi"],"Olarak Güncellenmiştir")
        guncellemeEkrandonus()    
    elif deger == 4:
        guncellenecekIndex  = int(input("Kişinin index numarasını giriniz: "))
        guncellenecekKey    = "Telefon Numarası"

        oldName = kisiler[guncellenecekIndex][guncellenecekKey]
        kisiler[guncellenecekIndex][guncellenecekKey] = input("Kişinin yeni telefon numarasını giriniz: ")

        print("Kişinin yeni telefon numarası :", kisiler[guncellenecekIndex]["Telefon Numarası"],"Olarak Güncellenmiştir")
        guncellemeEkrandonus()
    elif deger == 5:
        anaekran()
    elif deger == 6:
        exit
    else:
        print("Lütfen düzgün bir değer giriniz")
        guncelleme()




def anaekran():
    print("""
    ####################-TELEFON REHBERİ-####################
    # --Kayıt eklemek için        (1)                       #
    # --Kayıt düzenlemek için     (2)                       #
    # --Kayıt silmek için         (3)                       #
    # --Kayıt listesi için        (4)                       #
    # --Arama için                (5)                       #
    # --Çıkış için                (6)                       #
    #########################################################
    """)
    islem = int(input("Lütfen yapmak istediğiniz işlemin numarasını giriniz: "))

    if islem == 1 :
        ekleme()
    elif islem ==2 :
        guncelleme()
    elif islem == 3 :
        kayitSilme()
    elif islem == 4 : 
        kayitListesi()
        anaEkranDonus()
    elif islem == 5 :
        pass
    elif islem == 6:
        print("********HOŞÇAKALIN********")
        exit
    else:
        print("Girdiğiniz işlem numarası geçersiz.")
        anaekran()

anaekran()