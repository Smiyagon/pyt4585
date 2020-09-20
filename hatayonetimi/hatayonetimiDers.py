# # Programcı Hataları (Error)
# # Program ksuruları
# # Istisnai Hataları 
# # Mantıksal hataları (En zor hatalardır.)



# try:
#     telefonNo = int(input("Lütfen Telefon numaranızı giriniz:  ")) 
#     print("Tebrikler")
# except ValueError:
#     print("ValueErr")
# except ZeroDivisionError:
#     print("Zero Division Error.") 
# except:
#     print("Sadece Sayısal Değer giriniz!!!")

try:
    sayi_bir = int(input("Lütfen 1.sayıyı giriniz: "))
    sayi_iki = int(input("Lütfen 2.sayıyı giriniz: "))

    toplam = sayi_bir + sayi_iki
    fark = sayi_bir - sayi_iki
    carpim = sayi_bir * sayi_iki
    bolum  = sayi_bir / sayi_iki
    mod  = sayi_bir % sayi_iki

    print(f"Sayıların Toplamı:{toplam}\nSayıların Farkı : {fark}\nSayıların Bölümü : {bolum}\nSayıların Bölüm Farkı : {mod}\nSayıların Çarpımı : {carpim}")

except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("Sıfıra Bölünme Hatası")
except FileExistsError:
    print("Dosya Bulunamadı")
except:
    print("Tüm hataları kabul ediyorum, özür dilerim.")




