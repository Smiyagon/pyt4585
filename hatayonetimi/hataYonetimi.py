try:
    telefon_numarasi = input("Lütfen telefon numaranızı giriniz : ")
# Telefon numarası veri tabanına kaydedildi
    print("Telefon numaranız :",int(telefon_numarasi))
except ValueError:
    print("İşlem hatası")
    print("Lütfen geçerli bir sayı giriniz")
except ZeroDivisionError:
    print("İşlem hatası")
    print("sıfıra bölünme hatası")



try:
    sayi_bir = int(input("Lütfen birinci sayıyı giriniz : "))
    sayi_iki = int(input("Lütfen ikinci sayıyı giriniz : "))

    toplam = sayi_bir + sayi_iki
    fark   = sayi_bir - sayi_iki
    bolum  = sayi_bir / sayi_iki
    carpim = sayi_bir * sayi_iki

    print(  "Sayıların Toplamı :",toplam,
          "\nSayıların Farkı   :",fark,
          "\nSayıların Bölümü  :",bolum,
          "\nSayıların Çarpımı :",carpim )

except (ValueError,SyntaxError):
    print("Value Error veya Syntax Error hatası")
except ZeroDivisionError:
    print("Zero Division Error hatası")
except FileExistsError:
    print("File Exists Error")
except:
    print("hata mesajı")


# Hata mesajı

try:
    sayi = int(input("Lütfe sadece sayısal veri giriniz : "))
    print("gelen sayı", sayi)
    #sayi = sayi / 0
    sayi = str(sayi) / 0
    print("İşlem sonu")

except ValueError as ex:
    print("ValueError")
    print("Sistem hata mesajı ",ex)
except ZeroDivisionError as ex:
    print("ZeroDivisionError")
    print("Sistem hata mesajı ",ex)
except Exception as ex:
    print("except")
    print("Sistem hata mesajı ",ex)


try:
    sayi_bir = int(input("Lütfen bölünecek sayıyı giriniz : "))
    sayi_iki = int(input("Lütfen bölecek olan sayıyı giriniz : "))
    sonuc = sayi_bir / sayi_iki

except ValueError as exp:
    print("İşlem hatası :",exp)
else:
    try:
        print(sayi_bir/sayi_iki)
        print(sonuc)
    except ZeroDivisionError:
        print("Sayı 0 değerine bölünemez!")


try:
    sayi = int(input("Sayı giriniz : "))
    print("Tebrikler!!!")


    # Connection.close()
except:
    print("Hata aldık")
    #Connection.close()
finally:
    print("Her işlem sonucunda çalışır")
    #Connection.close()