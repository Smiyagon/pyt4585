kisiler = [
    {
        "İndex No": 0,
        "İsim" : "Tarık",
        "Soyisim" : "Kotan",
        "Mail Adresi":"kotan_t@hotmail.com",
        "Telefon Numarası" : "05340886128"
    }
]

def ekleme():
    index = len(kisiler) - 1
    isim = input("İsim: ")
    soyisim = input("Soyisim: ")
    mail = input("Mail Adresi: ")
    telefon = input("Telefon Numarası: ")
    kisiler.append({"İndex No:": index,"İsim" : isim,"Soyisim" : soyisim,"Mail Adresi":mail,"Telefon Numarası" : telefon})
    print(f"{isim} adlı kişi eklendi.")
    return anaEkranDonus()

def anaEkranDonus():
    sonuc = input("Başka bir işlem yapmak istiyor musunuz ?(y/n): ")
    if sonuc =="y":
        return anaekran()
    elif sonuc =="n":
        exit
    else:
        print("Sadece 'y' veya 'n' değerlerini giriniz")

def guncellemeEkrandonus():
    sonuc = input("Başka bir güncelleme işlemi yapmak istiyor musunuz ?(y/n): ")
    if sonuc =="y":
        return guncelleme()
    elif sonuc =="n":
        exit
    else:
        print("Sadece 'y' veya 'n' değerlerini giriniz")

def kayitSilmeEkranDonus():
    sonuc = input("Başka bir kayıt silmek  istiyor musunuz ?(y/n): ")

    if sonuc =="y":
        return kayitSilme()
    elif sonuc =="n":
        exit
    else:
        print("Sadece 'y' veya 'n' değerlerini giriniz")

def kayitSilme():
    deger = int(input("Lütfen silinecek kişinin adını giriniz: "))
    sonuc = input("Bu kişiyi silmek istediğinize emin misiniz?(y/n):")
    if sonuc == "y":
        kisiler[deger].remove("İsim")
        print("Kişi silindi")
    elif sonuc == "n":
        print("Çıkış yapıldı")
        exit
    else:
        print("Lütfen düzgün bir değer giriniz")


def guncelleme():
    print("""
    Yapacağınız güncellemede kişinin;
    Adını değiştirmek için              (1)
    Soyismini değiştirmek için          (2)
    Mail Adresini değiştirmek için      (3)
    Telefon Numarasını değiştirmek için (4)
    Çıkış yapmak için                   (5)
    """)
    deger = int(input("Lütfen yapacağınız işlemin numarasını giriniz : "))
    guncellenecekIndex  = int(input("Kişinin index numarasını giriniz: "))

    if deger == 1:
        guncellenecekKey    = "İsim"

        oldName = kisiler[guncellenecekIndex][guncellenecekKey]
        kisiler[guncellenecekIndex][guncellenecekKey] = input("Kişinin yeni adını giriniz: ")

        print("Kişinin Yeni Adı :", kisiler[guncellenecekIndex]["İsim"],"Olarak Güncellenmiştir")
        guncellemeEkrandonus()
        

    elif deger == 2:
        guncellenecekKey    = "Soyisim"

        oldName = kisiler[guncellenecekIndex][guncellenecekKey]
        kisiler[guncellenecekIndex][guncellenecekKey] = input("Kişinin yeni soyismini giriniz: ")

        print("Kişinin Yeni soyadı :",kisiler[guncellenecekIndex]["Soyisim"],"Olarak Güncellenmiştir")
        guncellemeEkrandonus()

    elif deger == 3:
        guncellenecekKey    = "Mail Adresi"

        oldName = kisiler[guncellenecekIndex][guncellenecekKey]
        kisiler[guncellenecekIndex][guncellenecekKey] = input("Kişinin yeni mail adresini giriniz: ")

        print("Kişinin yeni mail adresi :", kisiler[guncellenecekIndex]["Mail Adresi"],"Olarak Güncellenmiştir")
        guncellemeEkrandonus()    
    elif deger == 4:
        guncellenecekKey    = "Mail Adresi"

        oldName = kisiler[guncellenecekIndex][guncellenecekKey]
        kisiler[guncellenecekIndex][guncellenecekKey] = input("Kişinin yeni telefon numarasını giriniz: ")

        print("Kişinin yeni telefon numarası :", kisiler[guncellenecekIndex]["Telefon Numarası"],"Olarak Güncellenmiştir")
        guncellemeEkrandonus()
    elif deger == 5:
        exit
    else:
        print("Lütfen düzgün bir değer giriniz")


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

def anaekran():
    islem = int(input("Lütfen yapmak istediğiniz işlemin numarasını giriniz: "))

    if islem == 1 :
        ekleme()
    elif islem ==2 :
        guncelleme()
    elif islem == 3 :
        kayitSilme()
    elif islem == 4 : 
        print(kisiler)
    elif islem == 5 :
        pass
    elif islem == 6:
        exit
    else:
        print("Girdiğiniz işlem numarası geçersiz.")

anaekran()