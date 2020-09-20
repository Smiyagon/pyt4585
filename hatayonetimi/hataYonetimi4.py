try:
    sayi1 = int(input("Lütfen Sayı Giriniz : "))
    sayi2 = int(input("Lütfen Sayı Giriniz : "))

    sonuc = sayi1 / sayi2
except ValueError as mahmud:
    print("İşlem Hatası.")
else:
    try:
        print(sayi1 / sayi2)
        print("islem Sonucu")
    except ZeroDivisionError as mahmud: 
        print(mahmud)
