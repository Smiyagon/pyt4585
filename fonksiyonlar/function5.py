import os 


def sayiGiris():
    cift_sayilar = []
    tek_sayilar =[]
    go_on ="y"
    while go_on == "y":
        sayi1 = float(input("Lütfen sadece sayısal değer giriniz : "))
        if sayi1 % 2 != 0:
            tek_sayilar.append(sayi1)
        else:
            cift_sayilar.append(sayi1)
        go_on = input("İşleme devam etmek istiyor musunuz (y/n):  ").lower()
    print(sayi1)
    return max(tek_sayilar) - min(cift_sayilar)

sonuc = sayiGiris()
print("işlem sonucu: ",sonuc)