try: 
    sayi = int(input("Lütfen sayısal Değerler Giriniz! : "))
    print("Gelen Sayı : " , sayi)
    sayi = sayi / 0
    print("işlem sonucu")
except ValueError as ex:
    print("Lütfen tekrar deneyiniz")
    print("Sistem mesajı : ",ex)
except Exception as ex: 
    print("İşlem Hatası")
    print("Sistem mesajı : " , ex)